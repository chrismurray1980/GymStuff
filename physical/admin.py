from django.contrib import admin
from .models import Physical, Macro

# Register physical app models
admin.site.register(Physical)
admin.site.register(Macro)