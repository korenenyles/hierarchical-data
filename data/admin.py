from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from data.models import Data
# Register your models here.
admin.site.register(Data, DraggableMPTTAdmin)