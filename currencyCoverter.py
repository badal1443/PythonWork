## Convert 1 currency to another
## From everapi.com, freecurrencyapi.com
import requests
import os
from dotenv import load_dotenv

load_dotenv()  #loads env variables from .env file
apikey=os.getenv("API_KEY")

BASE_URL=f"https://api.freecurrencyapi.com/v1/latest?apikey={apikey}&currencies=EUR%2CUSD%2CCAD"

