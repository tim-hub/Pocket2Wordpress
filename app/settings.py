import os

from dotenv import load_dotenv

load_dotenv()

POCKET_URL = 'https://getpocket.com/v3/get'
ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')
CONSUMER_KEY = os.environ.get('CONSUMER_KEY')

WP_URL = os.environ.get('WP_URL', 'http://localhost')
WP_USER = os.environ.get('WP_USER', 'a wp user')
# wordpress plugin is required on wordpress side
# https://wordpress.org/plugins/application-passwords/
WP_APP_PWD = os.environ.get('WP_APP_PWD', 'a wp application password')
