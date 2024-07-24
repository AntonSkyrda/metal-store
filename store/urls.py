from django.urls import path

from .views import (
    index,
    ProductListView,
    ProductDetailView
)

urlpatterns = [
    path("", index, name="index"),
    path("metal-circles/", ProductListView.as_view(), name="metal-circle-list"),
    path("metal-circles/<int:pk>/", ProductDetailView.as_view(), name="metal-circle-details")
]

app_name = "store"
