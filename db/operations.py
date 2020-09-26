from mysql.connector import Error as DBError

# Application Libraries
from settings import DB_CONF_FILE, DB_CONF_SECTION
from db.read_configuration import read_db_conf

def insert_registryRecord(cursor, transaction_id):
    """
        The function inserts record into the table registry of 
        the database retail. 
        Input Parameters:
            cursor - connection cursor
            transaction_id - transaction id
        Output:
            The function returns last_record_id value.
            In case of successful insertion the value of the last_record_id
            is greater that 0.
    """
    last_row_id = -1;
    username = read_db_conf(DB_CONF_FILE, DB_CONF_SECTION)['user']
    query = """
        INSERT INTO registry(
            transaction_id,
            username
        )
        VALUES( %s, %s )
    """
    
    try:
        cursor.execute(query, (transaction_id, username))
        last_row_id = cursor.lastrowid
    except DBError as err:
        print(err)
    finally:
        return last_row_id
    
def insert_retailTransactionRecord(cursor, retailTransactionObject):
    """
        The function inserts retail transaction record into the table
        called transactions.
        Input Parameters:
            cursor - connection cursor
            retailTransactionObject - retail transaction object. Object code is located
                in transaction/transactions.py.
        Output:
            The function returns last_row_id value. This value is positive in case
            of successful insertion.
    """
    last_row_id = -1;
    query = """
        INSERT INTO transactions(
            transaction_id,
            unit_id,
            workstation_id,
            sequence_id,
            begin_date_time,
            end_date_time,
            currency,
            quantity,
            extended_amount,
            net_amount,
            training_mode_flag
            )
        VALUES(
            '{0.id}',
            {0.unit_id},
            {0.workstation_id},
            {0.sequence_id},
            '{0.start_dtime}',
            '{0.end_dtime}',
            '{0.currency}',
            {0.quantity},
            {0.extended_amount},
            {0.transaction_net_amount},
            {0.training_mode_flag}
        )
    """.format(retailTransactionObject)
    try:
        cursor.execute(query)
        last_row_id = cursor.lastrowid
    except DBError as err:
        print(err)
    finally:
        return last_row_id

    
    
    
    
    
    
    
    
    