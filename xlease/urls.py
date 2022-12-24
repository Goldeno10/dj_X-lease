from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('countries', views.CountryViewSet)
router.register('states', views.StateViewSet)
router.register('cities', views.CityViewSet)
router.register('customers', views.CustomerViewSet)
router.register('categories', views.CategoryViewSet)
router.register('items', views.ItemViewSet)

items_router = routers.NestedDefaultRouter(
    router, 'items', lookup='item'
)
items_router.register('images', views.ItemImageViewSet, basename='item-images')
items_router.register('reviews', views.ReviewViewSet, basename='item-reviews')
urlpatterns = router.urls + items_router.urls