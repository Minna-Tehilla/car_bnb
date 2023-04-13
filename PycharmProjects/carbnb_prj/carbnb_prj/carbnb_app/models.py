from django.contrib.auth.models import User
from django.db import models


class Car (models.Model):
    plate_number = models.IntegerField (unique = True, default = 0000, db_index = True)
    type = models.CharField (null = False, max_length = 50)
    cost = models.IntegerField (null = False)
    owner = models.ForeignKey ("Person", on_delete = models.RESTRICT, related_name = 'car_owner', null = True)
    year = models.IntegerField (null = False)

    renters = models.ManyToManyField ("Person", through = "Rent",
                                      related_name = "rented_cars")

    class Meta:
        db_table = "car"
        indexes = [
            models.Index (fields = ["plate_number", "type"])
        ]

    def __str__(self):
        return f"<Car:{self.type} Id: {self.id}>"


class Person (models.Model):
    id = models.IntegerField (primary_key = True)
    # name = models.CharField (null = False, max_length = 50)
    address = models.CharField (null = False, max_length = 50)
    age = models.IntegerField (null = False)
    user = models.OneToOneField (on_delete = models.RESTRICT, null = False, related_name = "person_user",
                                 to = User)

    # user2 = models.ForeignKey (User, unique = True,on_delete = models.RESTRICT, null=True)

    class Meta:
        db_table = "person"

    def __str__(self):
        # return self.user.username
        return f"<Person:{self.user.username}, Id:{self.id}>"


class Rent (models.Model):
    start_date = models.DateTimeField (null = True, blank = True, auto_now = True)
    end_date = models.DateTimeField (null = True, blank = True)
    car = models.ForeignKey ("Car", on_delete = models.RESTRICT)
    client = models.ForeignKey (Person, on_delete = models.RESTRICT)

    class Meta:
        db_table = "rent"

    def __str__(self):
        return f"<Rent Id:{self.id}>"


class ContactMessage (models.Model):
    name = models.CharField (null = False, max_length = 50)
    email = models.EmailField (null = True, blank = True)
    title = models.CharField (null = False, max_length = 20)
    content = models.CharField (null = False, max_length = 2000)
    creation_date = models.DateTimeField (null = False, auto_now_add = True)

    class Meta:
        db_table = "contact_message"

    def __str__(self):
        return f" Message : {self.id}, {self.title}, {self.creation_date}"


class Bike (models.Model):
    plate_number = models.IntegerField (unique = True)
    year = models.IntegerField (null = False)
    factory = models.ForeignKey ("Factory", on_delete = models.RESTRICT)

    class Meta:
        db_table = "Bike"


class Factory (models.Model):
    name = models.CharField (unique = True, max_length = 30)
    address= models.CharField (max_length = 50)

    class Meta:
        db_table = "Factory"
