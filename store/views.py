from django.shortcuts import render
from django.views import generic

from .forms import ProductSearchForm
from .models import (
    Product,
)


class ProductListView(generic.ListView):
    model = Product
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = ProductSearchForm(
            initial={"name": name}
        )

        return context

    def get_queryset(self):
        queryset = Product.objects.all()
        form = ProductSearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(
                name__icontains=form.cleaned_data["name"]
            )

        return queryset


class ProductDetailView(generic.DetailView):
    model = Product
