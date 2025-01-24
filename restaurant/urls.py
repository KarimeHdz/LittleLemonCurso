from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import MenuItemView, SingleMenuItemView, MenuItemViewSet, BookingViewSet

router = DefaultRouter()
router.register(r'menu', MenuItemViewSet, basename='menuitem')
router.register(r'booking', BookingViewSet, basename='booking')

urlpatterns = [
    # Incluye las rutas generadas automáticamente por el enrutador
    path('', include(router.urls)),
    #path('menu/', MenuItemView.as_view()),
    # Ruta para obtener un token de autenticación
    path('api-token-auth/', obtain_auth_token),
]

#urlpatterns = [
    #path('', sayHello, name='sayHello'),
   # path('', views.index, name='index'),
 #   path('menu/', MenuItemView.as_view()),
  #  path('menu/<int:pk>', SingleMenuItemView.as_view()),
  #  path('api-token-auth/', obtain_auth_token),
  #  path('', include(router.urls)),
#]
