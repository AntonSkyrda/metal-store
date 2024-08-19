from .models import Category
from .forms import ProductSearchForm


def add_categories(request):
    categories = Category.objects.prefetch_related('categories').all()
    context = {
        'categories': [
            {
                'name': category.name,
                'products': category.categories.all()
            }
            for category in categories
        ]
    }
    return context


def product_search(request):
    return {"form": ProductSearchForm()}
