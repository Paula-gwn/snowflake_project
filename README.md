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
📁 Project Structure & Local Setup  
This project demonstrates a local data workflow that connects Snowflake, dbt, and Git in a structured and reproducible way. It is designed to follow best practices for analytics engineering.

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

🔗 Connecting Git and Snowflake Locally
✅ Git & GitHub
This repository is version-controlled using Git and hosted on GitHub for collaboration and project tracking.  
❄️ Snowflake Setup
Data is stored in Snowflake and queried through dbt.  
Steps taken:  
1. Created a Snowflake account and manually uploaded a CSV dataset
2. Created a table in Snowflake using the Snowflake UI or SQL
