from .models import Category


# def add_categories(request):
#     categories = Category.objects.all()
#
#     return {'categories': categories}


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
