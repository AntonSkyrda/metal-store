from django.contrib import admin

from .models import (
    Category,
    CategorySizes,
    Product,
    Sizes,
)

admin.site.register(Category)
admin.site.register(CategorySizes)
admin.site.register(Product)
admin.site.register(Sizes)
