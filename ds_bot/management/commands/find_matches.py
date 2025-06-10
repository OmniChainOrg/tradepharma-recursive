# ds_bot/management/commands/find_matches.py
from django.core.management.base import BaseCommand
from ds_bot.inventory.inventory import Offer, Demand, Match

class Command(BaseCommand):
    help = 'Find matches between open offers and demands'

    def handle(self, *args, **kwargs):
        offers = Offer.objects.filter(status='open')
        demands = Demand.objects.filter(status='open')

        for offer in offers:
            matches = demands.filter(
                product=offer.product,
                quantity__lte=offer.quantity,
                location=offer.location
            )

            for demand in matches:
                Match.objects.create(offer=offer, demand=demand)
                demand.status = 'matched'
                demand.save()
                offer.status = 'matched'
                offer.save()
                self.stdout.write(self.style.SUCCESS(f'Matched {offer} with {demand}'))

        self.stdout.write(self.style.SUCCESS('Matching complete'))
      
