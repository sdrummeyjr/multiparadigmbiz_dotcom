from django.contrib import admin
from .models import Topic, Entry, EntryType


# Register models here.
admin.site.register(Topic)
admin.site.register(Entry)
admin.site.register(EntryType)
