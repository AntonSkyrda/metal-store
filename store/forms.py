from django import forms

from store.models import Category


class ProductSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Пошук"
            }
        )
    )


class CategorySearchForm(forms.Form):
    category = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        required=False,
        label="Категорія",
        widget=forms.CheckboxSelectMultiple
    )
