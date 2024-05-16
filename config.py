import os
from dotenv import load_dotenv

load_dotenv()

HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
CABINET_TOKEN = os.getenv("CABINET_TOKEN")
CABINET_URL = os.getenv("CABINET_URL")
TIMEOUT = 60
