import os
import csv
import datetime
from mysql.connector import Error as DBError

# Application Libraries
from db.connection import get_db_connection
from settings import TRANSACTIONS_DAILY_REPORTS_DIR

def daily_transactions_summary(year=None, month=None, day=None):
    # Setting Reporting Date
    if year is None and month is None and day is None:
        reporting_date = datetime.date.today() - datetime.timedelta(days=1)
    else:
        reporting_date = datetime.date(year = year, month = month, day = day)
    
    # Setting Report file
    report_file_name = "{0}{1}{2}_transactions.csv".format(
        reporting_date.year, 
        reporting_date.month, 
        reporting_date.day)
    
    report_file_location = os.path.join(TRANSACTIONS_DAILY_REPORTS_DIR, report_file_name)
    if os.path.isfile(report_file_location):
        print("The report file already exists: \n\t{0}".format(report_file_location))
        print("Please delete the existing report in case you need to generate a new one.")
        return 1
    
    with open(report_file_location, "w+", newline="") as csv_report:
        header = ["Store ID", 
                  "Currency", 
                  "Total Quantity", 
                  "Total Net Amount", 
                  "Total Transactions"]
        writer = csv.DictWriter(csv_report, fieldnames=header)
        writer.writeheader()
    
    d1 = datetime.datetime(reporting_date.year, 
                           reporting_date.month, 
                           reporting_date.day, 0, 0, 0)
    
    d2 = d1 + datetime.timedelta(days=1)
    
    # Setting Reporting Query
    query = """
        SELECT unit_id as `Store ID`,
            currency as `Currency`,
            SUM(quantity) as `Total Quantity`,
            SUM(net_amount) as `Total Net Amount`,
            COUNT(transaction_id) as `Total Transactions`
        FROM transactions
        WHERE begin_date_time >= '{0}' AND begin_date_time < '{1}' 
            AND training_mode_flag = 0
        GROUP BY unit_id, currency
        ORDER BY unit_id;
        
    """.format(d1, d2)
    
    # Opening DB Connection
    dbconn = get_db_connection()
    # Open connection Cursor
    cursor = dbconn.cursor(dictionary=True)
    # Execute query
    try:
        cursor.execute(query)
    except DBError as err:
        print("Daily transactions query execution failed ({0})".format(
            datetime.date(reporting_date.year, reporting_date.month, reporting_date.day)))
        return 2
    
    for row in cursor:
        with open(report_file_location, "a", newline="") as csv_report:
            writer = csv.DictWriter(csv_report, fieldnames=header)
            writer.writerow(row)
            
    return 0
        
if __name__ == '__main__':
    daily_transactions_summary()
    