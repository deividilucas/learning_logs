from django.contrib import admin # type: ignore
from learning_logs.models import Topic, Entry


# Register your models here.

admin.site.register(Topic)
admin.site.register(Entry)
