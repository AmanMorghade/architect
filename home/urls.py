from django.urls import path
from .views import *
urlpatterns=[
    path('',home_page,name='home_page'),
    path('contact/',contact_view,name='contact'),

]