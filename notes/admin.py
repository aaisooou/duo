from django.contrib import admin
from .models import Note  # Импортируй модель Note

admin.site.register(Note)  # Зарегистрируй её
