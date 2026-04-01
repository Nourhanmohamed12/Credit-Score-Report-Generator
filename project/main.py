import sqlite3
import os

#RUN ADDdATA.PY FIRST


# Database file names
DB_FILES = {
    "user": "user_db.sqlite",
    "payments": "payments_db.sqlite",
    "debt": "debt_db.sqlite",
    "history": "history_db.sqlite",
    "mix": "mix_reference_db.sqlite"
}

# Function to calculate iScore
def calculate_credit_score(user_id):
    os.chdir("databases")
    
    # Get user name
    with sqlite3.connect(DB_FILES["user"]) as conn:
        cur = conn.cursor()
        cur.execute("SELECT name FROM users WHERE user_id = ?", (user_id,))
        user = cur.fetchone()
        if not user:
            os.chdir("..")
            return f"User ID {user_id} not found."

    # Payment history
    with sqlite3.connect(DB_FILES["payments"]) as conn:
        cur = conn.cursor()
        cur.execute("SELECT on_time_payments, total_payments FROM payments WHERE user_id = ?", (user_id,))
        result = cur.fetchone()
        paymentScore = (result[0] / result[1]) * 100 if result and result[1] else 0

    # Outstanding debt
    with sqlite3.connect(DB_FILES["debt"]) as conn:
        cur = conn.cursor()
        cur.execute("SELECT used_credit, credit_limit FROM debts WHERE user_id = ?", (user_id,))
        result = cur.fetchone()
        utilization = (result[0] / result[1]) if result and result[1] else 1
        debtScore = (1 - utilization) * 100

    # Credit history age
    with sqlite3.connect(DB_FILES["history"]) as conn:
        cur = conn.cursor()
        cur.execute("SELECT account_age, max_age FROM history WHERE user_id = ?", (user_id,))
        result = cur.fetchone()
        historyScore = (result[0] / result[1]) * 100 if result and result[1] else 0

    # Credit mix
    with sqlite3.connect(DB_FILES["mix"]) as conn:
        cur = conn.cursor()
        cur.execute("SELECT credit_types_used, total_types FROM credit_mix WHERE user_id = ?", (user_id,))
        result = cur.fetchone()
        mixScore = (result[0] / result[1]) * 100 if result and result[1] else 0

    os.chdir("..")

    # Final score calculation
    finalScore = (
        0.35 * paymentScore +
        0.30 * debtScore +
        0.15 * historyScore +
        0.20 * mixScore
    )

    scaledScore = 300 + ((finalScore / 100) * (850 - 300))

    return {
        "user_id": user_id,
        "name": user[0],
        "payment_score": round(paymentScore, 2),
        "debt_score": round(debtScore, 2),
        "history_score": round(historyScore, 2),
        "mix_score": round(mixScore, 2),
        "final_score": round(finalScore, 2),
        "scaled_score": round(scaledScore, 2)
    }


# Main
if __name__ == "__main__":
    user_id = int(input("Enter User ID: "))
    print(calculate_credit_score(user_id))
