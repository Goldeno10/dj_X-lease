from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Country, State, City, Customer, Category, Item
from .serializers import CountrySerializer, CustomerSerializer, StateSerializer, CitySerializer, CustomerSerializer, CreateCategorySerializer, ItemSerializer



class CountryViewSet(ModelViewSet):
    queryset = Country.objects.all().order_by('name')
    serializer_class = CountrySerializer

class StateViewSet(ModelViewSet):
    queryset = State.objects.all().order_by('name')
    serializer_class = StateSerializer

class CityViewSet(ModelViewSet):
    queryset = City.objects.all().order_by('name')
    serializer_class = CitySerializer

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CreateCategorySerializer

    # def get_serializer_context(self):
    #     return self.id


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all().order_by('name')
    serializer_class = ItemSerializer
