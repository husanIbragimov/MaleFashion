from django.contrib import admin
from .models import ColorCategory, SizeCategory, Category, Product, Rate, ProductImage, BandingCategory


class ColorCategoryAmin(admin.ModelAdmin):
    list_display = ('color_name', 'color', )


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


class RateInline(admin.TabularInline):
    model = Rate
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline, RateInline]
    filter_horizontal = ('color', 'size')


admin.site.register(Product, ProductAdmin)
admin.site.register(ColorCategory, ColorCategoryAmin)
admin.site.register(SizeCategory)
admin.site.register(Category)
admin.site.register(Rate)
admin.site.register(BandingCategory)



