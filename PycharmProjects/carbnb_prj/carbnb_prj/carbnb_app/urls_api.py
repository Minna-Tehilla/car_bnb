from django.urls import path
from . import views_api
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('message', views_api.serve_messages),
    path('signup', views_api.signup),
    path('private', views_api.private),
    path('car', views_api.CarApi),
    # path('car/get', views_api.CarApi.as_view(action='get')),
    # path('car/post', views_api.CarApi.as_view(action='post')),
    # path('car/put', views_api.CarApi.as_view(action='put')),
    # path('car/delete', views_api.CarApi.as_view(action='delete')),
    path('person', views_api.PersonApi.as_view()),
    path('rent', views_api.RentApi.as_view()),
    path('bike', views_api.bike),
    path('login', obtain_auth_token),
    path('home', views_api.home)
]
