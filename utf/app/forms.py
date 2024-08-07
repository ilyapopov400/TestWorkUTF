from django import forms
from . import models


class FoodCategoryForm(forms.ModelForm):
    """
    Форма для записи карточки сотрудника
    """

    class Meta:
        model = models.FoodCategory
        fields = "__all__"
        labels = {
            "name_ru": "Название на русском",
            "name_en": "Название на английском",
            "name_ch": "Название на китайском",

        }


class Food(forms.ModelForm):
    """
    Форма для записи карточки сотрудника
    """

    class Meta:
        model = models.Food
        fields = "__all__"
        labels = {
            "category": "Раздел меню",
            "is_vegan": "Вегетарианское меню",
            "is_special": "Специальное предложение",
            "code": "Код поставщика",
            "internal_code": "Код в приложении",
            "name_ru": "Название на русском",
            "description_ru": "Описание на русском",
            "description_en": "Описание на английском",
            "description_ch": "Описание на китайском",
            "cost": "Цена",
            "is_publish": "Опубликовано",
            "additional": "Дополнительные товары",

        }
