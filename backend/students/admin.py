from django.contrib import admin
from .models import students    

models_list = [students]
admin.site.register(models_list)

# 

