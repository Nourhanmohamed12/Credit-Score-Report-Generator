import sqlite3
import os
import streamlit as st

#RUN ADDdATA.PY FIRST
# to install dependencies pip install --upgrade pip --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host=files.pythonhosted.org
# to install dependencies pip install streamlit --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host=files.pythonhosted.org

#THEN TO RUN THIST WRITE IN TERMINAL streamlit run gui.py



# Database file names with paths
DB_DIR = "databases"
DB_FILES = {
    "user": os.path.join(DB_DIR, "user_db.sqlite"),
    "payments": os.path.join(DB_DIR, "payments_db.sqlite"),
    "debt": os.path.join(DB_DIR, "debt_db.sqlite"),
    "history": os.path.join(DB_DIR, "history_db.sqlite"),
    "mix": os.path.join(DB_DIR, "mix_reference_db.sqlite")
}

# Function to calculate credit score
def calculate_credit_score(user_id):
    # Get user name
    with sqlite3.connect(DB_FILES["user"]) as conn:
        cur = conn.cursor()
        cur.execute("SELECT name FROM users WHERE user_id = ?", (user_id,))
        user = cur.fetchone()
        if not user:
            return None

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

    # Final score
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

# Streamlit UI
st.set_page_config(page_title="Credit Score Analyzer", page_icon="📊")
st.title("📊 Credit Score Report Generator")

# Load users
with sqlite3.connect(DB_FILES["user"]) as conn:
    user_list = conn.execute("SELECT user_id, name FROM users").fetchall()

user_options = {f"{name} (ID: {uid})": uid for uid, name in user_list}
selected_user = st.selectbox("Select a user", list(user_options.keys()))

if st.button("Generate Report"):
    user_id = user_options[selected_user]
    result = calculate_credit_score(user_id)

    if result:
        st.subheader(f"📄 Report for {result['name']} (User ID: {result['user_id']})")
        st.markdown(f"""
        **1. Payment History Score (35%)**: {result['payment_score']}  
        **2. Outstanding Debt Score (30%)**: {result['debt_score']}  
        **3. Credit History Age Score (15%)**: {result['history_score']}  
        **4. Credit Mix Score (20%)**: {result['mix_score']}  
        
        ### ✅ Final Weighted Score: {result['final_score']} / 100  
        ### 🏦 Credit Score: {result['scaled_score']} / 850
        """)
    else:
        st.error("User not found in the database.")
