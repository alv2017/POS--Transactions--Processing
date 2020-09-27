# POS Transactions Processing

The application reads retail transaction data from XML files, 
and stores them in the MySQL database. XML files examples are presented in the project directory called sample_data.

1) As per specification of the **Component 1**, a function

**process_retail_transaction_file(xmlFileLocation)**

takes an XML file as an input of the POSLog format, 
scans it for necessary data (Retail Transaction data) and stores it in a MySQL/MariaDB database table.

The function is located in incoming_transactions_processing.py file.

2) As per specification of the Component 2 script

**transactions_daily_report.py** 

is expected to run once a day, to scan the database table above, and to produce a csv file 
with sales grouped by store. 

**Output fields**: StoreID, TotalItems, TotalAmount, TotalReceipts.
At the moment the Date field is not presented in the report, however the names of the csv reports
will be contain the reporting date. (I'm going to fix this problem soon.)

**Comment**: In order to run the script on a daily basis we need to create a CRON job.
Currently it has to be run on the next day after actual reporting day. For example
if the script is running on 2020-10-02, then it will produce the report for the 2020-10-01.

