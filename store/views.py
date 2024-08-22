from django.shortcuts import render
from django.views import generic

from .forms import ProductSearchForm, CategorySearchForm
from .models import (
    Product,
)


class ProductListView(generic.ListView):
    model = Product
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        name = self.request.GET.get("name", "")
        categories = self.request.GET.getlist("category")

        context["search_form"] = ProductSearchForm(initial={"name": name})
        context["category_form"] = CategorySearchForm(initial={"category": categories})

        return context

    def get_queryset(self):
        queryset = Product.objects.all().select_related("category")

        name_form = ProductSearchForm(self.request.GET)
        if name_form.is_valid():
            name = name_form.cleaned_data.get("name")
            if name:
                queryset = queryset.filter(name__icontains=name)

        category_form = CategorySearchForm(self.request.GET)
        if category_form.is_valid():
            categories = category_form.cleaned_data.get("category")
            if categories:
                queryset = queryset.filter(category__in=categories)

        return queryset


class ProductDetailView(generic.DetailView):
    model = Product
