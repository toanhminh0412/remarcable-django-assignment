from django.db import models

# NOTES:
# - null=False, blank=False are by default but I want to be specific
class Category(models.Model):
    """
    Product categories
    Assuming one product falls into one category only
    """
    name = models.CharField(max_length=200, null=False, blank=False)

class Tag(models.Model):
    """
    Product tags
    Assuming one product can have multiple tags and one tag
    can belong to multiple products
    """
    name = models.CharField(max_length=200, null=False, blank=False)

class Product(models.Model):
    """
    Individual products
    """
    # NOTES:
    # - Products should include images but exempted here as it's not mentioned
    # in the assignment description
    name = models.CharField(max_length=200, null=False, blank=False)
    price = models.FloatField(null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    tag = models.ManyToManyField(Tag)
