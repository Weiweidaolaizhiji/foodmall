from django.contrib import admin

from apps.operations.models import FoodComments,UserFavorite,UserMessage

admin.site.register(FoodComments)
admin.site.register(UserFavorite)
admin.site.register(UserMessage)