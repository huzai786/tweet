import time
import sys
import requests
import django
import os
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tweety.settings')
django.setup()

from automate.models import Quotes

def get_quote():
    quotes = [q.quote for q in Quotes.objects.all()] 
    _quote = random.sample(quotes, 1)
    return _quote[0]


if __name__ == '__main__':
    get_quote()    
