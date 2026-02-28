import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env", override=True)

print("Loaded Key:", os.getenv("GOOGLE_API_KEY"))
