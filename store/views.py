from django.shortcuts import render
from django.views import generic

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


def index(request):
    return render(request, "store/index.html")


class MetalCircleListView(generic.ListView):
    model = MetalCircle
    paginate_by = 10


class MetalCircleDetailView(generic.DetailView):
    model = MetalCircle


class MetalSheetListView(generic.ListView):
    model = MetalSheet
    paginate_by = 10


class MetalSheetDetailView(generic.DetailView):
    model = MetalSheet


class MetalPipeListView(generic.ListView):
    model = MetalPipe
    paginate_by = 10


class MetalPipeDetailView(generic.DetailView):
    model = MetalPipe
