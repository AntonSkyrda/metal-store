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
    path("", index, name="index"),
    path("metal-circles/", MetalCircleListView.as_view(), name="metal-circle-list"),
    path("metal-circles/<int:pk>", MetalCircleDetailView.as_view(), name="metal-circle-details")
]

app_name = "store"
