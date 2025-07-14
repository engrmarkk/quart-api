from dotenv import load_dotenv
import os

load_dotenv()

DB_URI = os.getenv("DB_URI")
SECRET_KEY = os.getenv("SECRET_KEY")
