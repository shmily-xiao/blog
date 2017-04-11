class Config(object):
    '''Base config class.'''
    pass

class ProdConfig(Config):
    """Production config class."""
    pass

class DevConfig(Config):
    """Devlopment config class."""
    # Open the DEBUG
    DEBUG = True

    # MySQL connection
    # database_type+driver://user:password@sql_server_ip:port/database_name
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:qazwsx1234@127.0.0.1:3306/blog'
