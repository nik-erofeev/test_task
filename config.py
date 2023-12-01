import os
from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.environ.get("DB_NAME")
