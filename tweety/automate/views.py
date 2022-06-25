from django.shortcuts import render, redirect, HttpResponse
from automate.models import Tweets, Configr
from automate.forms import ConfForm, TweetForm
from get_tweet import get_tweet_data
import os
from packages.utils import store_cookies


def home(request):
    form = TweetForm()
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    tweets = Tweets.objects.all()
    ctx ={'tweets': tweets, 'form':form}
    return render(request, 'automate/home.html', ctx)


def delete_tweet(request, id):
    obj = Tweets.objects.get(id=id) 
    if request.method == 'POST':
        obj.delete()
        return redirect('home')
    ctx = {'obj': obj}
    return render(request, 'automate/delete_tweet.html', ctx)

def edit_tweet(request, id):
    tweet = Tweets.objects.get(id=id)
    form = TweetForm(instance=tweet)
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    ctx = {'form': form}
    return render(request, 'automate/edit_tweet.html', ctx)

def config(request):
    conf = Configr.objects.all()[0]
    ctx ={'conf': conf}
    return render(request, 'automate/conf.html', ctx)


def edit_conf(request):
    conf = Configr.objects.all()[0]
    form = ConfForm()
    if request.method == 'POST':
        form = ConfForm(request.POST, instance=conf)
        if form.is_valid():
            form.save()
            return redirect('conf')
    return render(request, 'automate/edit_conf.html', {'form':form})


def three_btns(request):
    if 'download_tweet' in request.POST:
        path = get_tweet_data()
        os.system(f'notepad.exe {path}')
        print('download tweets')

    if 'get_cookie' in request.POST:
        store_cookies()
        print('get cookie')
        
    return HttpResponse('<html><script>window.location.replace("/config/");</script></html>')

