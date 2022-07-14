import time
import sys
import requests
import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tweety.settings')
django.setup()
from automate.models import Quotes                        

def store_quotes():
    res = requests.get('https://zenquotes.io/api/random')
    if res.status_code == 200:
        if res.json()[0]['q'] != 'Too many requests. Obtain an auth key for unlimited access.':
            quote = res.json()[0]['q']
            try:
                Quotes.objects.create(quote=quote)
            except Exception as e:
                time.sleep(1)
        else:
            return


if __name__ == '__main__':
    try: 
        while True:
            time.sleep(1)
            print('storing quotes')
            store_quotes()
    except KeyboardInterrupt:
        sys.exit()
