from dotenv import load_dotenv
import os
load_dotenv()

POCKET_URL = 'https://getpocket.com/v3/get'
ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')
CONSUMER_KEY = os.environ.get('CONSUMER_KEY')