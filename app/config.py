import os

from dotenv import load_dotenv

load_dotenv()

LLM_API_KEY = os.getenv("LLM_API_KEY")
DATABASE_URL = os.getenv("DATABASE_URL")