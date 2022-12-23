from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from .models import Country, State, City, Customer, Category, Item, Review
from .serializers import CountrySerializer, CustomerSerializer, StateSerializer, CitySerializer, CustomerSerializer, CreateCategorySerializer, ItemSerializer, ReviewSerializer
from rest_framework.response import Response

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


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    @action(detail=False, methods=['GET', 'PUT'])
    def me(self, request):
        customer = Customer.objects.get(user_id=request.user.id)
        if request.method == 'GET':
            serializer = CustomerSerializer(customer)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = CustomerSerializer(customer, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return (serializer.data)




class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer
    def get_queryset(self):
        return Review.objects.filter(item_id=self.kwargs['items_pk'])
    
    def get_serializer_context(self):
        return {'item_id': self.kwargs['items_pk'], 'user_id': self.request.user.id}