from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ("name",)
        verbose_name_plural = "categories"

    def __str__(self):
        return f"{self.name}"


class Sizes(models.Model):
    size = models.PositiveIntegerField()

    class Meta:
        ordering = ("size",)
        verbose_name_plural = "sizes"

    def __str__(self):
        return f"{self.size}"


class CategorySizes(models.Model):
    name = models.CharField(max_length=255)
    size = models.ManyToManyField(Sizes, related_name="category_sizes", blank=True)

    class Meta:
        ordering = ("name",)
        verbose_name_plural = "categories sizes"

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    price = models.CharField(max_length=255)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="categories"
    )
    steel_mark = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)
    sizes = models.ManyToManyField(CategorySizes, related_name="sizes", blank=True)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return f"{self.name}"
