<div align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=28&pause=1000&color=60A5FA&center=true&vCenter=true&lines=Credit+Score+Analyzer;Financial+Insights+System;Python+%2B+SQLite+%2B+Streamlit+📊" />
  <br><br>
  <img src="https://img.shields.io/badge/💳-Credit%20Scoring-1E40AF?style=for-the-badge&logo=bank&logoColor=white" />
  <img src="https://img.shields.io/badge/📊-Data%20Analysis-3B82F6?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/⚡-Streamlit%20App-60A5FA?style=for-the-badge&logo=streamlit&logoColor=white" />
</div>

---

## <div align="center"><b style="color:#1E40AF">📊 Project Overview</b></div>

The **Credit Score Report Generator** is a **data-driven financial analysis system** that calculates and visualizes user credit scores based on multiple financial factors.

It integrates **Python**, **SQLite databases**, and **Streamlit UI** to simulate a real-world credit scoring model similar to banking systems.

The system evaluates users using:

* 💳 Payment history
* 💰 Debt utilization
* 📅 Credit history age
* 🔄 Credit mix

<div align="center">
  <img src="https://img.shields.io/badge/📊-Scoring%20System-60A5FA?style=for-the-badge" />
  <img src="https://img.shields.io/badge/🗄️-SQLite%20DB-3B82F6?style=for-the-badge" />
  <img src="https://img.shields.io/badge/🖥️-Interactive%20UI-1E40AF?style=for-the-badge" />
</div>

---

## ✨ **Key Features**

| Feature                   | Description                            |
| ------------------------- | -------------------------------------- |
| 👤 User Management        | Store and retrieve user data           |
| 💳 Credit Scoring         | Calculate score using weighted factors |
| 📊 Detailed Report        | Breakdown of each scoring component    |
| 🗄️ Multi-Database System | Separate SQLite DBs for modular design |
| 🖥️ Interactive UI        | Streamlit dashboard for easy use       |
| ⚡ Real-time Calculation   | Instant score generation               |

---

## 🧠 **Scoring Model**

The credit score is calculated using a weighted formula:

* **Payment History (35%)**
* **Debt Utilization (30%)**
* **Credit History Age (15%)**
* **Credit Mix (20%)**

Final score is scaled between **300 → 850**.

---

## 🖥️ **System Architecture**

graph TB
    A[👤 User Input] --> B[🖥️ Streamlit UI]
    B --> C[⚡ Python Logic]
    
    C --> D[🗄️ User DB]
    C --> E[💳 Payments DB]
    C --> F[💰 Debt DB]
    C --> G[📅 History DB]
    C --> H[🔄 Credit Mix DB]
    
    C --> I[📊 Score Calculation]
    I --> J[📄 Final Report]
```

---

## 📂 **Project Structure**

```
Credit-Score-Analyzer/
│
├── addData.py          # Setup databases and insert initial data
├── gui.py              # Streamlit UI application
├── main.py             # CLI-based credit score calculation
│
├── databases/
│   ├── user_db.sqlite
│   ├── payments_db.sqlite
│   ├── debt_db.sqlite
│   ├── history_db.sqlite
│   ├── mix_reference_db.sqlite
```

---

## ⚙️ **How It Works**

### 1️⃣ Database Setup

* Creates multiple SQLite databases
* Inserts sample users and financial data

### 2️⃣ Data Retrieval

* Fetches user data from different databases

### 3️⃣ Score Calculation

* Computes individual scores:

  * Payment score
  * Debt score
  * History score
  * Mix score

### 4️⃣ Final Credit Score

* Applies weighted formula
* Scales result to **300–850 range**

---

## 🚀 **Quick Start**

# 1. Clone the repository
git clone https://github.com/Nourhanmohamed12/Credit-Score-Report-Generator.git
cd credit-score-analyzer
```

### 🔧 Setup Databases


python addData.py


### ▶️ Run CLI Version


python main.py


### 🌐 Run Streamlit App


pip install streamlit
streamlit run gui.py



## 📊 **Example Output**

```
User: Ahmed

Payment Score: 90.0
Debt Score: 70.0
History Score: 30.0
Mix Score: 50.0

Final Score: 72.5
Credit Score: 698 / 850
```

---

## 📈 **Performance Highlights**

| Metric           | Value                     |
| ---------------- | ------------------------- |
| Response Time    | < 1s                      |
| Database Queries | Optimized                 |
| Scalability      | Modular DB Design         |
| Accuracy         | Rule-based weighted model |

---

## 🔮 **Future Enhancements**

* 🤖 Machine Learning Credit Prediction
* ☁️ Cloud Database Integration
* 📊 Advanced Data Visualization (Dashboards)
* 🔐 User Authentication System
* 📱 Mobile App Integration

---

## 👩‍💻 **Author**

<div align="center">
  <a href="https://linkedin.com/in/nour-mohammed-614753278">
    <img src="https://img.shields.io/badge/Nourhan%20Mohammed-1E40AF?style=for-the-badge&logo=linkedin&logoColor=white" />
  </a>
  <img src="https://img.shields.io/badge/B.Sc.%20Data%20Science-3B82F6?style=for-the-badge&logo=university&logoColor=white" />
</div>

---

## ❤️ **Acknowledgments**

<div align="center">
  <img src="https://img.shields.io/badge/💳-Credit%20Analytics-60A5FA?style=for-the-badge" />
  <br>
  <sub>Built with ❤️ for financial data analysis and system design</sub>
</div>

<div align="center">
  <img src="https://img.shields.io/badge/License-MIT-1E40AF?style=for-the-badge&logo=legal&logoColor=white" />
</div>
