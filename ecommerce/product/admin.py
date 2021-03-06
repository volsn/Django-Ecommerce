from django.contrib import admin
from product.models import Product, Color, Manufacturer, Image
# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_filter = ('top_selling', 'featured',)
    actions = ('set_top_selling', 'unset_top_selling',
               'set_features', 'unset_features',)

    def set_top_selling(self, request, queryset):
        queryset.update(top_selling=True)
    set_top_selling.short_description = 'Set as Top Selling'

    def unset_top_selling(self, request, queryset):
        queryset.update(top_selling=False)
    unset_top_selling.short_description = 'Unset Top Selling'

    def set_features(self, request, queryset):
        queryset.update(featured=True)
    set_features.short_description = 'Set as Featured'

    def unset_features(self, request, queryset):
        queryset.update(featured=False)
    unset_features.short_description = 'Unset Featured'


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    pass


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    pass


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass
