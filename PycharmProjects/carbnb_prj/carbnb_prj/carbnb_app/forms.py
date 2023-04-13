from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import Car, Person, Rent
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError


class DatePicker (forms.TextInput):
    input_type = "date"

class PersonCreationForm(forms.ModelForm):

    class Meta:
        model = Person
        exclude = ["user"]
        fields = "__all__"

class MyUserCreationForm(UserCreationForm):
    # email= forms.EmailField()
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "username"]


class Search (forms.Form):
    car_type_str = forms.CharField (max_length = 4, required = False, label = 'Car Type')
    year_str = forms.IntegerField (max_value = 2024, min_value = 1950)
    car_type = forms.CharField (widget = forms.TextInput (attrs = {"style": "background-color:red"}))

    email = forms.EmailField (required = False, initial = "mt@mt.com")

    I_agree_to_all_terms = forms.BooleanField ()

    gender = forms.ChoiceField (choices = [
        ("male", 'זכר'),
        ("male", 'נקבה')])

    cars = forms.ModelChoiceField (queryset = Car.objects.all ())

    date = forms.DateField (widget = forms.SelectDateWidget)
    date1 = forms.DateField (widget = DatePicker)


class Contact (forms.Form):
    file = forms.FileField (required = False, label = "Download your picture here")
    person_info = forms.ModelChoiceField (queryset = Person.objects.all ())

    cars = forms.ModelChoiceField (queryset = Car.objects.all ())
    Agree_to_receive_emails = forms.BooleanField ()
    Description_of_problem = forms.CharField (max_length = 500, required = False,
                                              widget = forms.Textarea (attrs = {"rows": 5}),
                                              validators = [RegexValidator ("[a-z]", message = "Letters only please")])


def already_exits(plate_number):
    cars = Car.objects.all ()
    for car in cars:
        # if car.plate_number==forms.ModelForm.plate_number:

        raise ValidationError (message = "This car already exists")


class CarForm (ModelForm):
    email = forms.EmailField (required = False)
    plate_number = forms.IntegerField (disabled = True)

    class Meta:
        model = Car
        fields = "__all__"  # (validators=already_exits())
        exclude = ['renters']


class EditCarForm (ModelForm):
    email = forms.EmailField (required = False)
    plate_number = forms.IntegerField (disabled = True)

    class Meta:
        model = Car
        fields = "__all__"


class LoginForm(forms.Form):
    username = forms.CharField (max_length = 20)
    password = forms.CharField (max_length = 20)
