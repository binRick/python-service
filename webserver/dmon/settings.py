PACKAGE_NAME = 'dmon'
API_PORT = 9001
API_HOST = '127.0.0.1'


# Import local settings
try:
    from local_settings import *
except ImportError:
    pass
