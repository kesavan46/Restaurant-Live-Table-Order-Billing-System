from django.db import models

class MenuItem(models.Model):

    class Category(models.TextChoices):
        STARTER = "STARTER", "Starter"
        MAIN = "MAIN", "Main"
        DRINKS = "DRINKS", "Drinks"
        DESSERT = "DESSERT", "Dessert"

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=Category.choices)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
