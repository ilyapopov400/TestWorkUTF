from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class Index(TemplateView):
    """
    - стартовая страница приложения
    """
    template_name = "app/index.html"
