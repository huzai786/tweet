import random
import string
import requests
import time
from datetime import datetime
import os
import pickle
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
import sys

sys.path.append('../')

from get_quotes import get_quote


l = ['🥶', '😱', '😨', '😥', '😓', '🤗', '🤔', '🤭', '🤫', '🤥', '😶', '😐', '😑', '😬', '🙄', '😯', '😦',
     '😧', '😮', '😲', '🥱', '😴', '🤤', '😪', '😵', '🤐', '🥴', '🤢', '🤮', '🤧', '😷', '🤒', '🤕', '🤑', '😉',
     '😌', '😍', '🥰', '😘', '😗', '😙', '😚', '😋', '😛', '😝', '😜', '🤪', '🤨']


def check_exists_by_xpath(driver, xpath):
    try:
        driver.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        return False
    return True


def return_emoji(no_of_emoji):
    return ''.join(random.sample(l, no_of_emoji))


def return_random_string(size=4, chars=string.digits + string.punctuation):
    return ''.join(random.choice(chars) for _ in range(size))


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
        quote_msg = get_quote()
        if quote_msg != '':
            msg += f'"{quote_msg}"'
    return msg
