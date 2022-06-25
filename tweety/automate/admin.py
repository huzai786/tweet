from django.contrib import admin
from automate.models import Tweets, Configr
from django.contrib.auth.models import Group, User


admin.site.register(Tweets)
admin.site.register(Configr)
admin.site.unregister(Group)
admin.site.unregister(User)


admin.site.site_header = "Twitter BOT"
admin.site.site_title = "Twitter BOT"
admin.site.index_title = "Twitter automation"