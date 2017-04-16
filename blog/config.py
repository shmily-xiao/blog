class Config(object):
    '''Base config class.'''
    SECRET_KEY = 'aad7b9b55a84265155322fe603b97168'

class ProdConfig(Config):
    """Production config class."""
    pass

class DevConfig(Config):
    """Devlopment config class."""
    # Open the DEBUG
    DEBUG = True

    # MySQL connection
    # database_type+driver://user:password@sql_server_ip:port/database_name
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:qazwsx1234@127.0.0.1:3306/blog'
