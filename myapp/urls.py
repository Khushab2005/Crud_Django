from django.urls import path,include
from myapp.views import *

urlpatterns = [
    path('',home_page,name='home_page'),
    path('insert/',insert,name="insert"),
    path('update/<int:id>/',update,name="update"),
    path('delete/<int:id>/',delete,name="delete"),
]
