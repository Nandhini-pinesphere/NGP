from django.db import models


class Food(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='food_images/')

    def __str__(self):
        return self.name
    
class Cart(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    def total(self):
        return self.quantity * self.price

