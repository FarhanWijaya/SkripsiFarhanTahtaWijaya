import os
from dotenv import load_dotenv

# Load environment variables from .env file
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
env_file = os.path.join(BASE_DIR, '.env')
if os.path.exists(env_file):
    load_dotenv(env_file)
else:
    load_dotenv()

class Config:
    # Flask configuration
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'kareem-net-super-secret-key-12345'
    
    # Database Configuration
    DB_USER = os.environ.get('DB_USER', 'root')
    DB_PASSWORD = os.environ.get('DB_PASSWORD', '')
    DB_HOST = os.environ.get('DB_HOST', 'localhost')
    DB_PORT = os.environ.get('DB_PORT', '3306')
    DB_NAME = os.environ.get('DB_NAME', 'kareem_monitoring')
    
    # Check if we should fallback to SQLite (useful for quick testing / development)
    # Default: True, but can be set to False in .env to use MySQL
    USE_SQLITE = os.environ.get('USE_SQLITE', 'True').lower() in ('true', '1', 't', 'y', 'yes')
    
    BASE_DIR = BASE_DIR
    
    if USE_SQLITE:
        SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}"
    else:
        # Default connection string using pymysql
        SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
            f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
            
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Upload limits and folders
    UPLOAD_FOLDER = os.path.join(BASE_DIR, 'app', 'static', 'uploads')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB limit
