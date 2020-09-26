import os

# APP SETTINGS

# Application Root Directory
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# DB configuration file location
DB_CONF_FILE = os.path.join(ROOT_DIR, "config", "config.ini")
# Configuration Section name
DB_CONF_SECTION = "mysql_retail_app"

# Daily Reports Directory
DAILY_REPORTS_DIR = os.path.join(ROOT_DIR, "daily_reports")

# Transactions Daily Summary
TRANSACTIONS_DAILY_REPORTS_DIR = os.path.join(DAILY_REPORTS_DIR, "transactions")
