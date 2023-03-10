from datetime  import timedelta
from django.contrib import admin
from django.urls import reverse
from django.db.models.aggregates import Count
from django.utils.html import format_html, urlencode
from .models import Country, State, City, Customer, Category, Item, Review


admin.site.site_header = "X-lease"

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone', 'birth_date']



@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['name', 'number_of_states']

    def number_of_states(self, instance):
        return State.objects.filter(country__id=instance.id).count()


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ['name', 'zipcode', 'country', 'number_of_cities']

    def number_of_cities(self, instance):
        return City.objects.filter(state__id=instance.id).count()


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['name', 'zipcode', 'state']

@admin.register(Category)
class CategoryAmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'updated_at', 'items_count']

    def items_count(self, category):
        url = (
            reverse('admin:xlease_item_changelist')
            + '?'
            + urlencode({
                'category__id': str(category.id)
            }))
        plural = 's' if category.items_count > 1 else ''
        return format_html('<a href="{}"> {} item{}</a>', url, category.items_count, plural)
    
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            items_count=Count('items')
        )


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price_per_day', 'owned_by', 'leased_to', 'lease_period', 'return_date', 'reviews_count']

    def return_date(self, item:Item):
        return item.updated_at + timedelta(days=item.lease_period)
    
    def reviews_count(self, item):
        url = (
            reverse('admin:xlease_review_changelist')
            + '?'
            + urlencode({
                'item__id': str(item.id)
            }))
        plural = 's' if item.reviews_count > 1 else ''
        return format_html('<a href="{}"> {} item{}</a>', url, item.reviews_count, plural)
    
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            reviews_count=Count('reviews')
        )

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['item_id', 'name', 'text', 'date']