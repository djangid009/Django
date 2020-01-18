from django.contrib import admin
from django.urls import path, include
from .views import home_page
# from .views import login
from .views import profile
from .views import blog
from .views import rank
from .views import questiondetails, question, log_out, profile

app_name = 'core'

urlpatterns = [
    path('', home_page),
    path('blog/', blog, name="blog"),
    path('rank/', rank, name="rank"),
    path('questiondetails/', questiondetails, name="questiondetails"),
    path('questions/', question),
    path('logout', log_out, name="logout"),
    path('profile', profile, name='profile')

]
