import random
import string
import requests
import time
from datetime import datetime
import pickle
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



l = ['🥶', '😱', '😨', '😥', '😓', '🤗', '🤔', '🤭', '🤫', '🤥', '😶', '😐', '😑', '😬', '🙄', '😯', '😦',
        '😧', '😮', '😲', '🥱', '😴', '🤤', '😪', '😵', '🤐', '🥴', '🤢', '🤮', '🤧', '😷', '🤒', '🤕', '🤑', '😉',
        '😌', '😍', '🥰', '😘', '😗', '😙', '😚', '😋', '😛', '😝', '😜', '🤪', '🤨']



def return_emoji(no_of_emoji):
    return ''.join(random.sample(l, no_of_emoji))
    
    
def return_random_string(size=4, chars=string.digits + string.punctuation):
    return ''.join(random.choice(chars) for _ in range(size))


def get_quotes():
    res = requests.get('https://zenquotes.io/api/random')
    if res.status_code == 200:
        if res.json()[0]['q'] != 'Too many requests. Obtain an auth key for unlimited access.':
            return res.json()[0]['q']
        else:
            return ''
    
        
def get_date():
    return str(datetime.now().strftime('%D %I %p'))


def add_tweet_variables(add_random_emoji, no_of_emoji, add_random_number, add_current_date, add_quotes):
    msg = ''
    if add_random_emoji:
        emoji_msg = return_emoji(no_of_emoji)
        msg += f'{emoji_msg}\n'
    if add_random_number:
        string_msg = return_random_string()
        msg += f'{string_msg}\n'
    if add_current_date:
        date_msg = get_date()
        msg += f'{date_msg} \n'
    if add_quotes:
        quote_msg = get_quotes()
        if quote_msg != '':
            msg += f'"{quote_msg}"'
    return msg


def store_cookies():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    driver.get('https://tweetdeck.twitter.com/')
    time.sleep(40)
    pickle.dump(driver.get_cookies(), open('cookies.pkl', 'wb'))
    

