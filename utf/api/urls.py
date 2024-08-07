from django.urls import path

from . import views

app_name = 'api'

urlpatterns = [
    path('api/v1/foods/', views.FoodApi.as_view()),

]
