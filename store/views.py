from django.shortcuts import render
from django.views import generic

from .models import (
    Product,
)


def index(request):
    return render(request, "store/index.html")


class ProductListView(generic.ListView):
    model = Product
    paginate_by = 10


class ProductDetailView(generic.DetailView):
    model = Product
