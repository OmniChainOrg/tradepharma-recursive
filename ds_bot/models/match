# ds_bot/models/match.py
from django.db import models
from .offer import Offer
from .demand import Demand

class Match(models.Model):
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    demand = models.ForeignKey(Demand, on_delete=models.CASCADE)
    matched_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(default='pending', max_length=255)

    def __str__(self):
        return f"Match {self.id}: {self.offer} - {self.demand}"
