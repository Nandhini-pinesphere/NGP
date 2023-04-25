from django.contrib import admin
from .models import Food , Cart

class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'image')
    list_filter = ('price',)
    search_fields = ('name', 'description')

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.order_by('-price')
        return queryset
    
class CartAdmin(admin.ModelAdmin):
    list_display=['food','image','quantity','price','total']

admin.site.register(Food, FoodAdmin)
admin.site.register(Cart, CartAdmin)


