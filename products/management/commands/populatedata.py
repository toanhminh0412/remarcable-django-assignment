import json
from django.core.management.base import BaseCommand, CommandError
from products.models import Category, Tag, Product


class Command(BaseCommand):
    """
    Django's management command to populate product data
    Prerequisite:
        data/products.json exists and has a proper JSON format
    
    Usage:
        python manage.py populatedata
    """
    help = "Populates product data from data/products.json"

    def handle(self, *args, **options) -> None:
        products = []
        with open("data/products.json", "r", encoding="utf-8") as f:
            products = json.load(f)

        # Create categories, tags and products in the database
        for product in products:
            try:
                name = product["name"]
                price = product["price"]
                description = product["description"]
                category = product["category"]
                tags = product["tags"]
            except KeyError as key_error:
                print(f"Invalid products.json. Missing a product key: {key_error}")
                return

            category, category_created = Category.objects.get_or_create(name=category)
            if category_created:
                print(f"Created a new category: {category.name}")

            new_product = Product.objects.create(
                name=name,
                price=price,
                description=description,
                category=category
            )

            for tag in tags:
                tag, tag_created = Tag.objects.get_or_create(name=tag)
                if tag_created:
                    print(f"Created a new tag: {tag.name}")

                new_product.tag.add(tag)

            print(
                "Created a new product:\n"
                f"- Name: {new_product.name}\n"
                f"- Price: {new_product.price}\n"
                f"- Description: {new_product.description}\n"
                f"- Category: {new_product.category.name}\n"
                f"- Tags: {new_product.render_tags()}\n"
            )
