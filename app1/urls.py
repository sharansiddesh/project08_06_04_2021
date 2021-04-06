from django.urls import path
from app1 import views

app_name="app1"


urlpatterns=[
    path('add/<num1>/<num2>',views.add,name="add"),
    path('fact/<num>',views.fact,name="fact")
]