from django.contrib import admin
from .models import Recipe , RecipeIngredient  
# Register your models here.

class RecipeIngredientsInline(admin.StackedInline):
    model = RecipeIngredient
    # fields = ['name','quantity','unit','description']
    extra = 0
    readonly_fields = ['quantity_as_float','as_mks','as_imperial']

class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientsInline]
    list_display = ['name']
    readonly_fields = ['timestamp', 'updated']
    raw_id_fields = ['user']

admin.site.register(Recipe, RecipeAdmin)
