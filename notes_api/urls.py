from django.contrib import admin
from django.urls import path, include  # Импортируем path и include
from rest_framework.authtoken import views
# Добавление пути для документации Swagger
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

# Создаем схему Swagger
schema_view = get_schema_view(
   openapi.Info(
      title="Notes API",
      default_version='v1',
      description="Документация API для заметок",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),  # Путь к админке Django
    path('api/', include('notes.urls')),  # Путь к API
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  # Путь для Swagger UI
    path('api-token-auth/', views.obtain_auth_token),
]
