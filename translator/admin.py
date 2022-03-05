from django.contrib import admin
from .models import Dictionary
# Register your models here.


class DictionaryAdmin(admin.ModelAdmin):
    list_display = ["english", 'uzbek']


admin.site.register(Dictionary, DictionaryAdmin)

