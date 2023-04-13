import json

from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.views.decorators.http import require_http_methods

from .models import Car, Person, Rent
from django.db.transaction import atomic
from django.shortcuts import get_object_or_404
from .forms import Search, Contact, CarForm, EditCarForm, LoginForm, PersonCreationForm, MyUserCreationForm
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


def default(req):
    # return HttpResponseRedirect(reverse("search_car"))
    return redirect ("https://www.kore.co.il")
    # return redirect ("contact")


def cars(req):
    car_type = Car.objects.all ()
    print ([car for car in car_type])
    return render (template_name = 'cars.html', request = req, context = {'car_type': car_type})


def car_by_id(req, id):
    cars = Car.objects.filter (id = id)
    # this is the query I want to make- how??
    # query = "select * from Car where Car.id==id"

    return render (template_name = 'car_by_id.html', request = req, context = {'car_by_id': cars})

def base(req):
    return  render(template_name = "base.html", request = req)


def search_car(req):
    if req.method == 'GET':
        return render (request = req, template_name = 'search_car.html', context = {'form': Contact})
    elif req.method == 'POST':
        return HttpResponse ('not submitted')


def search(req):
    if req.method == 'GET':
        return render (request = req, template_name = 'search_car.html')
    elif req.method == 'POST':
        search_str = req.POST['search_str'][0]
        cars = Car.objects.filter (type__contains = search_str)
        return render (template_name = 'cars_list.html', request = req, context = {"cars": cars}
                       )

        # return HttpResponse('not submitted')


def contact(req):
    if req.method == 'GET':
        return render (request = req, template_name = 'contact.html', context = {'form': Contact})
    elif req.method == 'POST':
        form = Contact (data = req.POST)
        file = req.FILES.get ('file')
        with open (str (settings.BASE_DIR) + fr"\carbnb_app\uploaded_files\{file.name}", "wb") as fh:
            for chunk in file.chunks ():
                fh.write (chunk)
            return HttpResponse ("file uploaded")

        if form.is_valid ():
            return JsonResponse (form.cleaned_data)
            # return HttpResponse(json.dumps(form.cleaned_data), mimetype="application/json")
            # return HttpResponse(req.POST)
        else:
            return render (request = req, template_name = 'contact.html', context = {'form': form})

        # return HttpResponse(str(req.POST))


def home(req):
    with atomic ():
        """here you write all of the logic that you want to happen as one block"""

        return HttpResponse ("")


def add_car(req):
    if req.method == "GET":
        return render (request = req, template_name = "add_car.html", context = {"form": CarForm ()})
    elif req.method == 'POST':
        form = CarForm (data = req.POST)
        if form.is_valid ():
            try:
                form.save ()
            except Exception as e:
                return HttpResponse (f" Error {e} has occurred")
            return HttpResponse ("Car Added Successfully!!!!!!")
        else:
            return render (request = req, template_name = 'add_car.html', context = {"form": form})
        # return render (request = req, template_name = 'add_car.html', context = {"form": form})


# Create your views here.

def edit_car(req, plate_number):
    if req.method == "GET":
        car = Car.objects.get (plate_number = plate_number)  # todo:deal with exceptions
        form = CarForm (instance = car)
        # form = CarForm (instance = car)
        return render (request = req, template_name = "edit_car.html",
                       context = {"form": form, 'plate_number': plate_number})  # CarForm ()})
        # return render (request = req, template_name = "add_car.html", context = {"form": form,'plate_number':plate_number })#CarForm ()})
    elif req.method == 'POST':
        try:
            # form = CarForm(data = req.POST)
            car = Car.objects.get (plate_number = plate_number)
            form = CarForm (instance = car, data = req.POST)
            # form = CarForm (instance = car)
            if form.is_valid ():
                form.save ()
                return HttpResponse ("Car information has been edited Successfully!!!!!!")

            else:
                return render (request = req, template_name = 'edit_car.html',
                               context = {"form": form, 'plate_number': plate_number})

        except Exception as e:
            return HttpResponse (f" Error {e} has occurred", status = 500)

        # return render (request = req, template_name = 'add_car.html', context = {"form": form})


@require_http_methods (['GET'])
def display_cars(req):
    cars = Car.objects.all ()

    return render (request = req, template_name = 'cars_list.html', context = {'cars': cars})


from django.views.generic import CreateView, ListView, DeleteView, UpdateView


class CarsListView (ListView):
    model = Car
    template_name = 'car_list.html'
    context_object_name = 'car_list'
    queryset = Car.objects.filter (type__contains = "t")


class PersonCreateForm (CreateView):
    model = Person
    template_name = 'person_form.html'
    fields = "__all__"
    success_url = "/admin"


class DisplayListView (ListView):
    model = Car
    template_name = 'cars_list.html'
    context_object_name = 'cars'
    # queryset = Car.objects.filter(type__contains="t")


class PersonUpdateView (UpdateView):
    model = Person
    fields = "__all__"
    template_name = 'person_update.html'
    success_url = "/admin"

#
# def home2(req):
#     if req.user.is_authenticated:
#         return HttpResponse (f"Welcome {req.user}")
#     else:
#         return HttpResponse (f"Welcome anonymous user!")
#     # req.session['session_key'] = "session_value"
#     # return HttpResponse ( f"Hello home , {req.session.keys()}")

# @login_required()
def home2(req):
        return HttpResponse (f"Welcome {req.user}!")

def create_user(req):
    if req.method == 'GET':
        # return render (request = req, template_name = "login.html",
        #                context = {"form": LoginForm(), 'action': 'signup'})
        return render (request = req, template_name = "signup.html",
                       context = {"user_form": MyUserCreationForm,
                                  "person_form": PersonCreationForm})
    elif req.method == 'POST':
        user_form = MyUserCreationForm(data = req.POST)
        person_form = PersonCreationForm(data= req.POST)
        if user_form.is_valid() and person_form.is_valid():
            user = user_form.save()
            person_form.instance.user = user
            person_form.save()
            login(request = req,user = user)
            return redirect("home2")
        else:
            return render (request = req, template_name = "signup.html",
                           context = {"user_form": user_form,
                                      "person_form": person_form})

        # un = req.POST.get ("username")
        # pw = req.POST.get ("password")
        # user = User.objects.create_user(username = un, password = pw)
        # login(request = req, user = user)
        # return redirect('home2')
        # form = UserCreationForm (data = req.POST)
        # if form.is_valid:
        #     form.save ()
        #     login (request = req, user = form.instance)
        #     return redirect ('home2')
        # else:
        #     return render (request = req, template_name = "signup.html",
        #                    context = {"form": UserCreationForm ()})


def connect(req):
    if req.method == 'GET':
        return render (request = req, template_name = "login.html", context = {"form": LoginForm (), 'action': 'login'})
    elif req.method == 'POST':
        un = req.POST.get ("username")
        pw = req.POST.get ("password")
        user = authenticate (req, username = un, password = pw)
        if user is None:
            return HttpResponse ("Wrong user info")
        else:
            login (request = req, user = user)
            return HttpResponse (f"Welcome {user.username}")


def logout_user(req):
    if req.user.is_authenticated:
        logout (request = req)
        return HttpResponse ("Logged out")
