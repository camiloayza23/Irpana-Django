from django.contrib import admin
from .models import Lugar
from .models import Highlights
from .models import Tipos
# Register your models here.

admin.site.register(Highlights)
admin.site.register(Tipos)
admin.site.register(Lugar)