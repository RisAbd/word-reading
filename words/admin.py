from django.contrib import admin

from . import models


@admin.register(models.Word)
class WordAdmin(admin.ModelAdmin):

    list_display = '__str__ enabled audio'.split()