from django.contrib import admin
from forum.models import *

# Register your models here.
@admin.register(
    Thread, 
    Comment, 
)
class UniversalAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.concrete_fields]