from django.urls import path
from . import views
from django.views.generic import CreateView,ListView
from .views import add_car
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # path("",views.default),
    path ("", views.home2, name='home2'),
    path ("base", views.base, name = 'base'),
    # path('login', views.connect, name= 'login'),
    path ('login', LoginView.as_view(), name = 'login'),
    path('signup', views.create_user, name= 'signup'),

    # path('logout', views.logout_user, name= 'logout'),
    path('logout', LogoutView.as_view(), name= 'logout'),
    path('cars', views.cars),
    path('car/id', views.car_by_id,name='car_by_id'),
    path('search_car', views.search_car, name='search_car'),
    path('search', views.search, name='search_car'),
    path('contact', views.contact, name='contact'),
    path('add_car', views.add_car,name='add_car'),
    path ('edit_car/<str:plate_number>', views.edit_car, name = 'edit_car'),
    path('cars_list',views.display_cars, name='cars_list'),
    path('car_list',views.CarsListView.as_view()),
    path('create_person',views.PersonCreateForm.as_view(),name='create_person'),
    path('display_list',views.DisplayListView.as_view(), name='display_list'),
    path ('update_person/<int:pk>', views.PersonUpdateView.as_view (), name = 'update_person'),


]