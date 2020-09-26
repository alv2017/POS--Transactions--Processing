from mysql.connector import MySQLConnection, Error as DBError
# Application Libraries
from settings import DB_CONF_FILE, DB_CONF_SECTION
from db.read_configuration import read_db_conf


def get_db_connection():
    """ Connects to MySQL DB: retail
        and returns MySQLConnection object
    """
    conn = None
    db_conf_settings = read_db_conf(DB_CONF_FILE, DB_CONF_SECTION)
    try:
        conn = MySQLConnection(**db_conf_settings)
        if conn.is_connected():
            return conn
        else:
            raise Exception("Connection: DB Connection failed: {}".format(db_conf_settings["database"]))
    except DBError as err:
        print(err)
        return None