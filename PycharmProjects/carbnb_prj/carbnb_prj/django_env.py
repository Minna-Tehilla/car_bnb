import os
import time

os.environ.setdefault ("DJANGO_SETTINGS_MODULE",
                       "carbnb_prj.settings")  # make sure it is this and not "my_project.settings"
import django

django.setup ()

from carbnb_app.models import *
from django.contrib.auth.models import User
#
# car = Car.objects.first ()
# # print(car.renters.all()) # who rented the cars
# # print(car.owner.name) #shows the name of car owner
# p = car.owner
# print (p)
# print (
#     p.car_owner.all ())  # represents all cars that are owned by this person, maybe more correct to change this related name to owned cars
#
# p = car.renters.first ()
# # print(p.rented_cars.all()) # show how many cars this person rented
# print(User.objects.all())
# u = User.objects.create_user(username = "Meir",password = "0000")
# print(u)

persons = Person.objects.all()

for p in persons:
    if not p.user:
        # user = User.objects.create_user (username = f"{time.time()}", password = "123")
        # user.delete()

        user = User.objects.create_user(username = f"{time.time()}", password = "123")
        p.user = user
        p.save()
