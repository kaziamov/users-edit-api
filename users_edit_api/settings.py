import dotenv
import os
from urllib.parse import urlparse


dotenv.load_dotenv()


DATABASE_URL = urlparse(os.environ.get('DATABASE_URL'))

DB_HOST = DATABASE_URL.hostname
DB_PORT = DATABASE_URL.port
DB_NAME = DATABASE_URL.path[1:]
DB_USER = DATABASE_URL.username
DB_PASS = DATABASE_URL.password
