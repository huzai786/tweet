import django 
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tweety.settings')
django.setup()

from automate.models import Tweets
tweets = Tweets.objects.all()


def get_tweet_data():
    with open('tweet_data.txt', 'w', encoding='utf-8', newline='') as f:
        for t in tweets:
            f.write(f'{t.tweet}\n--------------------------------------\n')
    return os.getcwd() + '\\tweet_data.txt'


if __name__ == '__main__':
    get_tweet_data()
    
    