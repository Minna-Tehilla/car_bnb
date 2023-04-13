from django.contrib import admin
from .models import Car, Person, Rent, ContactMessage, Bike, Factory
from django.contrib.sessions.models import Session
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission

admin.site.register(Person)
admin.site.register(Car)
admin.site.register(Rent)
admin.site.register(Session)
admin.site.register(ContentType)
admin.site.register(Permission)
admin.site.register(ContactMessage)
admin.site.register(Bike)
admin.site.register(Factory)


