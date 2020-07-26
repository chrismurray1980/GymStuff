from django.db import models

from products.models import Product

class customer_review(models.Model):
    RATING_CHOICES = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    username = models.CharField(max_length=200)
    comment = models.TextField()
    rating = models.IntegerField(choices=RATING_CHOICES)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment