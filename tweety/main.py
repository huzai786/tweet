
import os
import time
import django
from datetime import datetime
from selenium import webdriver
from packages.schedule_tweet import TweetAutomation
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from rich.console import Console
from rich import print
from rich.traceback import install
from rich.prompt import Prompt
from rich.padding import Padding
from rich.progress import track
install()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tweety.settings')
django.setup()

from automate.models import Tweets

tweets = [{'tweet': tweet.tweet, 'img': str(
    tweet.my_PRF_image)} for tweet in Tweets.objects.all()]


console = Console()


def start_script():
    console.log('welcome to tweet automation, select your Configuration:',
                style="bold blue underline", highlight=True)
    print()
    interval = Prompt.ask("[bold italic underline red blink]Interval between tweets (minutes)[/bold italic underline red blink]",
                          choices=['5', '10', '15', '20', '25', '30'])
    time.sleep(0.5)
    Schedule_till = Prompt.ask("[bold italic underline red blink]Schedule till (months)[/bold italic underline red blink]",
                               choices=['1', '3', '6', '8', '12'])
    time.sleep(0.5)
    Add_emoji = Prompt.ask("[bold italic underline red blink]Add random emoji[/bold italic underline red blink]",
                           choices=['yes', 'no'])
    time.sleep(0.5)
    if Add_emoji.lower() == 'yes':
        no_of_emoji = Prompt.ask(
            "[bold italic underline red blink]Number of emojis [/bold italic underline red blink]", choices=['3', '4', '5', '6', '7', '8'], default=4)
    else:
        no_of_emoji = None
    random_character = Prompt.ask("[bold italic underline red blink]Add random character [/bold italic underline red blink]",
                                  choices=["yes", 'no'])
    Add_current_date = Prompt.ask("[bold italic underline red blink]Add current date [/bold italic underline red blink]",
                                  choices=["yes", 'no'])
    add_quotes = Prompt.ask("[bold italic underline red blink]Add quotes[/bold italic underline red blink]",
                            choices=['yes', 'no'])
    print()
    if Add_emoji == 'yes':
        add_random_emoji = True
    else:
        add_random_emoji = False

    if random_character == 'yes':
        add_random_number = True
    else:
        add_random_number = False

    if Add_current_date == 'yes':
        add_current_date = True
    else:
        add_current_date = False

    if add_quotes == 'yes':
        add_quotes = True
    else:
        dd_quotes = False

    console.log('Loading accounts credentials from file (accounts.txt)...',
                style="bold green", highlight=True)
    with console.status('setting up account settings', spinner='runner') as status:
        with open('accounts.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
        console.log(f'Found {len(lines)} account(s)',
                    style="bold green", highlight=True)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    with console.status("tweeting around...", spinner="earth"):
        for i, v in enumerate(lines):
            gmail, username, password = v.split(':')
            console.log(
                f'Account number {i}\n gmail: {gmail}\nusername: {username}', style="bold green", highlight=True)
            console.log('------------------------------------------')
            bot = TweetAutomation(driver, gmail, username, password)
            bot.login_and_credentials_process()
            bot.page_setup()
            bot.tweet_automation(tweets, int(interval), int(Schedule_till), add_random_emoji,
                                 no_of_emoji, add_random_number, add_current_date, add_quotes)


if __name__ == '__main__':
    start_script()
