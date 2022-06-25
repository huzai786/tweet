from django.forms import ModelForm
from django import forms
from automate.models import Configr, Tweets

class ConfForm(ModelForm):
    class Meta:
        model = Configr
        fields = '__all__'


class TweetForm(ModelForm):
    class Meta:
        model = Tweets
        fields = '__all__'