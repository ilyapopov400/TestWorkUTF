from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
from . import models
from . import forms


class Index(TemplateView):
    """
    - стартовая страница приложения
    """
    template_name = "app/index.html"

    def get_context_data(self, *args, **kwargs):
        """
        - добавили в контекст "food_category" -> список категорий для блюд
        :param args:
        :param kwargs:
        :return:
        """
        context = super().get_context_data(*args, **kwargs)
        food_categories = models.FoodCategory.objects.all()

        foods = models.Food.objects.all()

        context["food_categories"] = food_categories
        context["foods"] = foods

        return context
