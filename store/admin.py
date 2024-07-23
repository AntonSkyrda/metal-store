from django.contrib import admin

from .models import (
    Category,
    SubCategory,
    MetalCircle,
    MetalCircleSizes,
    MetalSheet,
    MetalSheetsSizes,
    MetalPipe,
    MetalPipeSizes,
)

admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(MetalCircle)
admin.site.register(MetalCircleSizes)
admin.site.register(MetalSheet)
admin.site.register(MetalSheetsSizes)
admin.site.register(MetalPipe)
admin.site.register(MetalPipeSizes)
