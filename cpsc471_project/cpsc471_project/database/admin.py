from django.contrib import admin
from .models import Club, Swimmer, Group, Coach, Admin, GroupPractices, Competition, EventRecord, Event, Entry

# Register your models here.
admin.site.register(Club)
admin.site.register(Swimmer)
admin.site.register(Group)
admin.site.register(Coach)
admin.site.register(Admin)
admin.site.register(GroupPractices)
admin.site.register(Competition)
admin.site.register(EventRecord)
admin.site.register(Event)
admin.site.register(Entry)