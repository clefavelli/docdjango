from django.contrib import admin
from .models import Board , Order , Gas , Order_State


admin.site.register(Board)
admin.site.register(Order)
admin.site.register(Gas)
admin.site.register(Order_State)

# Register your models here.
