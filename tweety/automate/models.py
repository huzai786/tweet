from django.db import models
from ckeditor.fields import RichTextField

duration_choices = (
    (5 ,'5 minute'),
    (10, '10 minute'),
    (15, '15 minute'),
    (25, '25 minute'),
    (30, '30 minute'),
)

schedule_duration = (
    (30, '1 month'),
    (90, '3 month'),
    (180, '6 month'),
    (365, '1 year'),
)

class Tweets(models.Model):
    tweet = models.TextField(max_length=150, blank=True, null=False)
    img = models.ImageField(null=True, blank=True, upload_to='images')
    
    def __str__(self):
        return str(self.tweet)[:50]
    
    class Meta:
        verbose_name_plural = 'tweets'
        
    @property
    def my_PRF_image(self):
        if self.img:
            return self.img.path
        return 'No image'
        
        
class Configr(models.Model):
    duration = models.IntegerField('Interval between tweets', choices=duration_choices)
    schedule_till = models.IntegerField(choices=schedule_duration)
    add_random_emoji = models.BooleanField('Add random emoji', default=True, null=True, blank=True)
    no_of_emoji = models.IntegerField(default=6, null=True, blank=True)
    add_random_number = models.BooleanField(default=True, null=True, blank=True)
    add_current_date = models.BooleanField(default=True, null=True, blank=True)
    add_quotes = models.BooleanField(default=True, null=True, blank=True)
    
    def __str__(self):
        return "Configuration settings"
    
    class Meta:
        verbose_name_plural = 'bot configuration'