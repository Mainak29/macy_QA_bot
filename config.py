from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")