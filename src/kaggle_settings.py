import os

from dotenv import load_dotenv

load_dotenv(verbose=True)

print(os.getenv("KAGGLE_USERNAME"))
