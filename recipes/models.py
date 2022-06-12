from django.db import models
from django.conf import settings
from .validators import validate_unit_of_measure
from .utils import number_str_to_float
import pint
# Create your models here.

class Recipe(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE)
    name = models.CharField(max_length=220)
    description = models.TextField(blank=True, null=True)
    directions = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def get_absolute_url(self):
        return '/pantry/recipes/'


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    name = models.CharField(max_length=220)
    quantity = models.CharField(max_length=50) # 1 1/4
    quantity_as_float = models.FloatField(blank=True, null=True)
    unit = models.CharField(max_length=50, validators=[validate_unit_of_measure]) # punds, lbs , oz , gram etc..
    description = models.TextField(blank=True, null=True)
    directions = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def get_absolute_url(self):
        return self.recipe.get_absolute_url()


    def convert_to_system(self, system='mks'):
        ureg = pint.UnitRegistry(system=system)
        if self.quantity_as_float is None:
            self.quantity_as_float = ''
        measurements = self.quantity_as_float * ureg[self.unit]
        return measurements.to_base_units()

    def as_mks(self):
        measurements = self.convert_to_system('mks')
        return measurements.to_base_units()


    def as_imperial(self):
        measurements = self.convert_to_system('imperial')
        return measurements.to_base_units()


    def save(self,*args,**kwargs):
        qty = self.quantity
        qty_as_float, qty_as_float_success = number_str_to_float(qty)
        if qty_as_float_success:
            self.quantity_as_float = qty_as_float
        super().save(*args,**kwargs)
