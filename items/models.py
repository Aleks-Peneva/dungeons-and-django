from django.db import models

# Create your models here.
class Items(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    type = models.CharField() # add options for items types, e.g. weapon, ammo, potion, arcane...
    notes = models.TextField(blank=True, null=True)
    discovered = models.BooleanField(default=False)
    # add fk for player, quest etc.