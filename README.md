# 🎮 Snowflake Project: Player Session Data Analysis

This project analyzes online player session data using **Snowflake**, **dbt**, and **Power BI** to generate insights such as average session duration, 7-day retention, and overall player engagement.

---

## 📊 Project Overview

- **Dataset**: Simulated CSV data of online player sessions
- **Cloud Data Platform**: [Snowflake](https://app.snowflake.com/xnvfqeu/go36229/#/data/databases/PLAYER_SESSIONS)
- **Transformation Layer**: dbt (data build tool)
- **Visualization**: Power BI
- **Automation**: Simple cron job or scheduler to refresh data daily

---

## 🏗️ Folder Structure
snowflake_project/
├── data/           # Raw CSV data  
│ └── player_sessions_mock.csv    
├── scripts/        # Python scripts  
│ └── load_data.py  
├── dbt_project/  
│ ├── dbt_project.yml  # dbt config  
│ └── models/  
│ ├── staging/      # Raw → Cleaned  
│ │ └── stg_sessions.sql  
│ └── marts/        # Aggregated metrics  
│ └── session_metrics.sql    
├── reports/        # Visual dashboards    
│ └── power_bi_dashboard.pbix  
├── cron_jobs/      # Task automation (e.g., daily updates)  
│ └── refresh_data.sh  
├── .gitignore  
├── requirements.txt  
└── README.md
