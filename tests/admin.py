from django.contrib import admin
from .models import Test


class TestAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'is_valid')


admin.site.register(Test, TestAdmin)
