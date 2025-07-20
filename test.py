
#├── data/                            # Raw CSV
#├── scripts/
#│   └── load_data.py                 # Python script to load data into Snowflake
#├── dbt_project/
#│   ├── models/
#│   │   ├── staging/                 # Clean raw tables
#│   │   └── marts/                   # Metrics like avg session time
#│   └── dbt_project.yml              # dbt config
#├── reports/
#│   └── power_bi_dashboard.pbix      # Your dashboard file
#├── cron_jobs/                      # .sh file for daily run (if Linux/Mac)
#├── README.md
#└── requirements.txt
