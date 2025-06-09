from django.db import models
from django.utils.timezone import now

class Company(models.Model):
    name = models.CharField(max_length=255, unique=True)
    contact_email = models.EmailField()
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Companies"


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Offer(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=50,
        default='open',
        choices=[('open', 'Open'), ('matched', 'Matched'), ('closed', 'Closed')]
    )
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.product.name} - {self.quantity} units by {self.company}"


class Demand(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    max_price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=50,
        default='open',
        choices=[('open', 'Open'), ('matched', 'Matched'), ('closed', 'Closed')]
    )
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.product.name} demand - {self.quantity} units by {self.company}"


class Match(models.Model):
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    demand = models.ForeignKey(Demand, on_delete=models.CASCADE)
    matched_at = models.DateTimeField(default=now)
    status = models.CharField(
        max_length=50,
        default='pending',
        choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('declined', 'Declined')]
    )

    def __str__(self):
        return f"Match: {self.offer} ↔ {self.demand}"
