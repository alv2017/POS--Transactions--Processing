from configparser import ConfigParser

def read_db_conf(conf_file, section):
    """
        The function reads database configuration data
        from the configuration file, and returns 
        database settings dictionary.
        Input Parameters:
            conf_file - configuration file location
            section - configuration file section where application
                      database settings are written
        Output:
            DB settings dictionary.
            The settings are used to establish the connection 
            to the application database
    """
    parser = ConfigParser()
    parser.read(conf_file)
    
    db = {}
    if parser.has_section(section):
        db_settings = parser.items(section)
        for setting in db_settings:
            db[setting[0]] = setting[1]
    else:
        raise Exception("[{0}] section was not found in the file: \n{1}.".format(section, conf_file))
    return db

if __name__=="__main__":
    sample_config_file = "../config/config_example.ini"
    section = "mysql"
    db_settings = read_db_conf(sample_config_file, section)
    print(db_settings)
    
    
    
