from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('countries', views.CountryViewSet)
router.register('states', views.StateViewSet)
router.register('cities', views.CityViewSet)
router.register('contacts', views.CustomerViewSet)
router.register('categories', views.CategoryViewSet)
router.register('items', views.ItemViewSet)

urlpatterns = router.urls