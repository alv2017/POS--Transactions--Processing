import os
import xml.etree.ElementTree as ET

# Application Libraries
from settings import ROOT_DIR
from transaction.parsers import retail_transaction_parser, XMLNS
from transaction.transactions import RetailTransaction
from db.connection import get_db_connection
from db.operations import insert_registryRecord, insert_retailTransactionRecord

def process_retail_transaction_file(xmlFileLocation):
    """
        The function processes XML files that contain 
        RetailTransaction elements. Then transaction data
        is loaded into retail database. The retail transaction record
        is saved to transactions table, and it is also registered within
        registry table.
        Input Parameters:
            xmlFileLocation - location of the XML file that needs to be processed
        Output:
            a) If the xml file is not found - the function returns 1
            b) If DB connection fails to establish - the function returns 2
            c) In all other cases the function returns 0
    """    
    nRetailTransactions = 0
    nSavedToDB = 0
    
    print("\n*** Started processing the file: \n\t{0}\n".format(xmlFileLocation))
    
    # Check if file exists
    if not os.path.isfile(xmlFileLocation):
        print("ERROR: XML file does not exist: \n\t{0}".format(xmlFileLocation))
        return 1
    
    # Read XML file
    tree = ET.parse(xmlFileLocation)
    root = tree.getroot()
    transactions = root.findall("poslog_ns:Transaction", XMLNS)
    
    # Establish DB connection
    dbconn = get_db_connection()
    if not dbconn:
        print("ERROR: Unable to establish DB connection.")
        return 2
    # Open db cursor
    cursor = dbconn.cursor()
    
    # Process transactions data
    for t in transactions:
        registry_record = -1
        transaction_record = -1
        # Open db cursor
        cursor = dbconn.cursor()
        # Process data
        transaction_dict = retail_transaction_parser(t)
        if not transaction_dict:
            continue
        nRetailTransactions = nRetailTransactions + 1
        retailTransactionObject = RetailTransaction.create_from_dictionary(transaction_dict)
        
        transaction_record = insert_retailTransactionRecord(cursor, retailTransactionObject)
        registry_record = insert_registryRecord(cursor, retailTransactionObject.id)
            
        if transaction_record > 0 and registry_record > 0:
            dbconn.commit()
            cursor.close()
            nSavedToDB = nSavedToDB + 1
            print("Transaction {0}: loaded successfully.".format(retailTransactionObject.id))
        else:
            print("\n    *************** FAILED TRANSACTION ***************")
            print("    Transaction {0}: loading to DB failed.".format(retailTransactionObject.id))
            print("    Failed to load transaction data:")
            print(retailTransactionObject)
            print("    **************************************************\n")
            dbconn.rollback()
    
    print("    File {0} has been processed.".format(xmlFileLocation))
    print("    Number of retail transactions: {0}".format(nRetailTransactions))
    print("    Number of retail transactions saved to retail database is {0}.".format(nSavedToDB))
    print()
    dbconn.close()
    return 0
        
if __name__ == '__main__':
    import sys
    if len(sys.argv)==1:
        print("Error: not enough argurments: Which xml files do you need to process?")
        print("\tUsage: python {0} file1.xml [file2.xml, ...]".format(sys.argv[0]))
    for i in range(1, len(sys.argv)):
        process_retail_transaction_file(sys.argv[i])
    
