"""
- В выборку попадают только Блюда у которых is_publish=True.
- Если в категории нет блюд (или все блюда данной категории имеют is_publish=False) - не включаем ее в выборку.
"""

from rest_framework import generics

from app.models import FoodCategory, Food
from .serializers import FoodListSerializer, FoodSerializer


# Create your views here.

class FoodApi(generics.ListAPIView):
    queryset = FoodCategory.objects.all()
    serializer_class = FoodListSerializer
