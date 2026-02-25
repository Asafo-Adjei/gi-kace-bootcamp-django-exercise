from django.db import models
from django.conf import settings

# Create your models here.

class Item(models.Model):
    # """
    # Model representing a marketplace item.
    # """

    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    # Owner (linked to Django User)
    owner = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE
)

    phone_number = models.CharField(max_length=15)

    # Product image
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    # Admin controls active/inactive
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title