import os

# Environment Variables
DATABASE_URL = os.getenv('DATABASE_URL')
SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = os.getenv('DEBUG', 'False') == 'True'

# Configuration Constants
API_VERSION = 'v1'
DEFAULT_PAGE_SIZE = 10
TIME_ZONE = 'UTC'
