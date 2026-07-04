# 📊 Care Transition Efficiency & Placement Outcome Analytics

> **A Machine Learning & Data Analytics project developed as part of the Unified Mentor Internship.**

## 📌 Project Overview

The **Care Transition Efficiency & Placement Outcome Analytics** project analyzes the operational efficiency of the **Unaccompanied Children (UAC) Program** managed by the **U.S. Department of Health and Human Services (HHS)**.

Instead of simply monitoring the number of children in care, this project evaluates how efficiently children move through the complete care pipeline—from **CBP custody** to **HHS care** and finally to **Sponsor Placement**.

The project transforms raw operational data into meaningful performance metrics, helping identify delays, bottlenecks, and overall system efficiency through an interactive Streamlit dashboard.

---

# 🎯 Problem Statement

Traditional reports focus on the number of children currently in custody but do not evaluate the efficiency of the transition process.

Important operational questions include:

* How efficiently are children transferred from CBP to HHS?
* Are sponsor placements keeping pace with incoming cases?
* Where do care backlogs occur?
* Is the overall care pipeline becoming more efficient over time?

This project answers these questions using data analytics and interactive visualizations.

---

# 🏗️ Project Architecture

```text
care-transition-analytics/
│
├── .gitignore
├── README.md
│
├── data/
│   └── raw/
│
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── metrics_engine.py
│   └── visualizations.py
│
├── app/
│   ├── main.py
│   └── modules/
│       ├── __init__.py
│       ├── pipeline_flow.py
│       ├── efficiency_panels.py
│       ├── bottleneck_charts.py
│       └── outcome_trends.py
│
└── reports/
    ├── UAC_Operational_Efficiency_Study.md
    └── Executive_Briefing.txt
```

---

# 📂 Dataset Description

The dataset contains daily operational information from the UAC care pipeline.

| Column                                         | Description                                  |
| ---------------------------------------------- | -------------------------------------------- |
| Date                                           | Reporting date                               |
| Children Apprehended and Placed in CBP Custody | Daily intake volume                          |
| Children in CBP Custody                        | Current children under CBP care              |
| Children Transferred Out of CBP Custody        | Daily transfers to HHS                       |
| Children in HHS Care                           | Current children receiving HHS care          |
| Children Discharged from HHS Care              | Children successfully reunited with sponsors |

---

# 🎯 Project Objectives

* Measure CBP → HHS transfer efficiency
* Evaluate discharge effectiveness
* Identify operational bottlenecks
* Analyze backlog accumulation
* Monitor pipeline throughput
* Provide actionable operational insights

---

# 📊 Key Performance Indicators (KPIs)

The dashboard automatically calculates the following metrics.

### 1. Transfer Efficiency Ratio (TER)

Measures the efficiency of transferring children from CBP to HHS.

```
Transfer Efficiency =
Transfers from CBP
-------------------
Children in CBP
```

---

### 2. Discharge Effectiveness Index (DEI)

Measures sponsor placement efficiency.

```
Discharge Effectiveness =
Discharges
------------
HHS Care
```

---

### 3. Pipeline Throughput

Measures overall movement through the care pipeline.

```
Pipeline Throughput =
Discharges
------------
Apprehended
```

---

### 4. Net Backlog Velocity

Measures whether unresolved cases are increasing.

```
Net Backlog =
Apprehended
-
Discharged
```

---

# 📈 Dashboard Features

The Streamlit dashboard provides:

* 📅 Date Range Filtering
* 📊 KPI Cards
* 🔄 Care Pipeline Monitoring
* 📈 Transfer Efficiency Analysis
* 📉 Discharge Effectiveness Tracking
* 🚦 Bottleneck Detection
* 📆 Weekly Trend Analysis
* 📅 Monthly Trend Analysis
* 📉 Backlog Monitoring
* 📌 Operational Insights

---

# 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Streamlit
* Matplotlib
* Seaborn
* Plotly

---

# ⚙️ Installation

Clone the repository.

```bash
git clone https://github.com/Mounish-24/care-transition-analytics.git
```

Move into the project directory.

```bash
cd care-transition-analytics
```

Install dependencies.

```bash
pip install pandas numpy matplotlib seaborn plotly streamlit
```

---

# ▶️ Run the Project

Launch the Streamlit dashboard.

```bash
streamlit run app/main.py
```

---

# 📊 Analysis Performed

The project performs:

* Data Cleaning
* Data Validation
* Exploratory Data Analysis (EDA)
* Pipeline Flow Analysis
* Efficiency Analysis
* Bottleneck Detection
* Backlog Trend Analysis
* Weekly & Monthly Trend Analysis
* Operational KPI Monitoring

---

# 📌 Key Insights

* Transfer efficiency varies across reporting periods.
* Sponsor placement performance directly impacts backlog accumulation.
* Days with higher intake often correspond to increased operational pressure.
* Continuous KPI monitoring enables early detection of process delays.
* Data-driven insights can support faster reunification and improved case management.

---

# 💡 Recommendations

* Improve transfer coordination between CBP and HHS.
* Increase sponsor placement efficiency during high-intake periods.
* Monitor backlog growth using KPI dashboards.
* Use real-time analytics to support operational decision-making.
* Prioritize early intervention when efficiency metrics decline.

---

# 📚 Future Improvements

* Machine Learning–based backlog forecasting
* Predictive discharge analysis
* Pipeline Health Score
* Automated anomaly detection
* Interactive executive reports
* PDF report generation
* Cloud deployment
* Real-time dashboard updates

---

# 👨‍💻 Author

**Mounish V**

B.Tech – Artificial Intelligence & Data Science

Machine Learning Intern – Unified Mentor

GitHub: https://github.com/Mounish-24/care-transition-analytics.git

---

# 📄 License

This project is developed for educational and internship purposes as part of the **Unified Mentor Machine Learning Internship**.
