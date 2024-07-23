from django.urls import path

from .views import (
    index,
    MetalCircleListView,
    MetalSheetListView,
    MetalPipeListView,
    MetalCircleDetailView,
    MetalSheetDetailView,
    MetalPipeDetailView,
)

urlpatterns = [
    path("", index, name="index")
]

app_name = "store"
