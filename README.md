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
Currently it has to be run on the next day after the actual reporting day. For example
if the script is running on 2020-10-02, then it will produce the report for the 2020-10-01.

# How to run the scripts?

### XML files processing

The script **incoming_transactions_processing.py** can be run from the command line
providing the location of the xml file as a parameter. 

**Example:**

Navigate to the project root folder and issue the following command:
```
python3 incoming_transactions_processing.py sample_data/arts1.xml
```

This will process the file **arts1.xml**, and the data from the file will be loaded
to the 'retail' database. The database contains two tables 'registry' and 'transactions',
and both tables will be populated with the corresponding data.

### Retail Transactions Daily Summary

The script should be run from the command line. The easiest would be to cd to the 
root project folder, and issue the following command:
```
python3 transactions_daily_report.py
```

It is also possible to run the script by providing the absolute path to it.

# Running Application using Docker

You can run and test the application by using docker containers.
In this case you need:

a) download a Dockerfile;

b) build Docker image from the downloaded docker file:
```
docker build . -t relyits_test
```

You need to run this command from the directory that contains the downloaded Docker file.

c) Run the docker container using newly created image:
```
docker run --name relyits_test_container relyits_test
```

For the first time I advise to run the container in attached mode. It takes 
some time till container starts, and it is a good idea
to follow the actions log and observe what is actually happening behind the scene.

d) When the container is up and running open another terminal window and log into it
using bash:
```
docker exec -it relyits_test_container bash
```

e) If things went as expected you should be logged in as root into the container. 
Next navigate to application root directory:
```
cd /opt/POS/POS_Transactions
```

Finally try to run the following command:

```
python3 incoming_transactions_processing.py sample_data/arts1.xml
```

If things go well you well load the data from arts1.xml into mysql database, 
and get a success message to the terminal:
```
*** Started processing the file: 
	sample_data/arts1.xml

Transaction 1907220000300457201001192000: loaded successfully.
    File sample_data/arts1.xml has been processed.
    Number of retail transactions: 1
    Number of retail transactions saved to retail database is 1.
```
    
    