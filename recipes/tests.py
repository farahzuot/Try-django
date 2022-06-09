from django.test import TestCase

from django.contrib.auth import get_user_model
from .models import Recipe, RecipeIngredient
# Create your tests here.

User = get_user_model()

class UserTestCase(TestCase):
    def setUp(self):
        self.user_a = User.objects.create_user('fuffy', password='farah123')

    def test_user_pw(self):
        checked = self.user_a.check_password('farah123')
        self.assertTrue(checked)

class RecipeTestCase(TestCase):
    def setUp(self):
        self.user_a = User.objects.create_user('fuffy', password='farah123')
        self.recipe_a = Recipe.objects.create(
            name='Grilled Chicken',
            user=self.user_a
        )
        self.recipe_b = Recipe.objects.create(
            name='Grilled Chicken Tacos',
            user=self.user_a
        )
        self.recipe_ingredient = RecipeIngredient.objects.create(
            recipe=self.recipe_a,
            name='chicken',
            quantity='1/5',
            unit='pound'
        )


    def test_user_count(self):
        qs = User.objects.all()
        self.assertEqual(qs.count(),1)

    def test_user_recipe_reverse_count(self):
        user = self.user_a
        qs = user.recipe_set.all()
        self.assertEqual(qs.count(),2)

    def test_user_recipe_forward_count(self):
        user = self.user_a
        qs = Recipe.objects.filter(user=user)
        self.assertEqual(qs.count(),2)

    def test_recipe_ingredients_reverse_count(self):
        recipe = self.recipe_a
        qs = recipe.recipeingredient_set.all()
        self.assertEqual(qs.count(),1)

    def test_recipe_ingredients_forward_count(self):
        recipe = self.recipe_a
        qs = RecipeIngredient.objects.filter(recipe=recipe)
        self.assertEqual(qs.count(),1)
