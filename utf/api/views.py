"""
- В выборку попадают только Блюда у которых is_publish=True.
- Если в категории нет блюд (или все блюда данной категории имеют is_publish=False) - не включаем ее в выборку.
"""

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from app.models import FoodCategory, Food
from .serializers import FoodListSerializer, FoodSerializer


# Create your views here.

# class FoodApi(generics.ListAPIView):
#     queryset = FoodCategory.objects.all()
#     serializer_class = FoodListSerializer

# queryset = Food.objects.filter(is_publish=True)
# serializer_class = FoodSerializer

class FoodApi(APIView):
    def get(self, request):
        result = list()
        food_categories = FoodCategory.objects.all()
        foods = Food.objects.all()
        for categories in food_categories:
            cat_dc = dict()
            cat_dc["pk"] = categories.pk
            cat_dc["name_ru"] = categories.name_ru
            cat_dc["name_en"] = categories.name_en
            cat_dc["name_ch"] = categories.name_ch
            cat_dc["order_id"] = categories.order_id
            cat_dc["foods"] = list()
            result.append(cat_dc)

        for food in foods:
            food_dc = dict()
            food_dc["is_vegan"] = food.is_vegan  #
            food_dc["is_special"] = food.is_special  #
            food_dc["code"] = food.code  #
            food_dc["internal_code"] = food.internal_code  #
            food_dc["name_ru"] = food.name_ru  #
            food_dc["description_ru"] = food.description_ru  #
            food_dc["description_en"] = food.description_en  #
            food_dc["description_ch"] = food.description_ch  #
            food_dc["cost"] = food.cost  #
            food_dc["is_publish"] = food.is_publish
            # food_dc["additional"] = food.additional  #

            for category in result:
                if category.get("pk") == food.category.pk and food.is_publish:

                    category.get("foods").append(food_dc)

        return Response(result)
