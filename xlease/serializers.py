from .models import Customer, Country, State, City, Category, Item, Review
from rest_framework import serializers


class CustomerSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Customer
        fields = ['id', 'user_id', 'phone', 'country', 'state', 'city']



class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'name']

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ['id', 'name', 'zipcode', 'country']

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'name', 'zipcode', 'state']


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'category', 'price_per_day', 'owned_by', 'leased_to', 'description']
      
class CreateCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

   
class CategorySerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField('cat_items')
    class Meta:
        model = Category
        fields = ['id', 'name', 'items']
    
    def cat_items(self, category: Category):
        return category.items

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'name', 'text', 'date']
    
    # def create(self, validated_data):
    #     return super().create(validated_data)
    #     item_id = self.context['item_id']
    #     user_id = self.contex['user_id']
    #     return Review.objects.create(user_id=user_id, item_id=item_id, **validated_data)