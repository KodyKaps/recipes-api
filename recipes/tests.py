from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from .models import Recipe

class RecipeListViewTests(TestCase):
    #setup method creates the data in the "database context"
    def setUp(self):
        Recipe.objects.create(
            name="Spaghetti Bolognese",
            ingredients="spaghetti, beef, tomato",
            cooking_time=30,
            difficulty="Medium",
            image_url="http://example.com/spaghetti.jpg"
        )
        Recipe.objects.create(
            name="Grilled Cheese",
            ingredients="bread, cheese, butter",
            cooking_time=5,
            difficulty="Easy",
            image_url="http://example.com/grilled_cheese.jpg"
        )
    #if i get the recipe list endpoint the response should be a success
    def test_recipe_list_status_code(self):
        """Test that the recipe list view returns a 200 response."""
        response = self.client.get(reverse('recipe_list'))
        self.assertEqual(response.status_code, 200)

    def test_template_used(self):
        """Test that the correct template is used."""
        response = self.client.get(reverse('recipe_list'))
        self.assertTemplateUsed(response, 'recipes/recipe_list.html')

    def test_recipes_in_context(self):
        """Test that recipes are present in the context and rendered."""
        response = self.client.get(reverse('recipe_list'))
        self.assertContains(response, "Spaghetti Bolognese")
        self.assertContains(response, "Grilled Cheese")

    def test_search_functionality(self):
        """Test that the search query filters results correctly."""
        response = self.client.get(reverse('recipe_list'), {'q': 'Spaghetti'})
        self.assertContains(response, "Spaghetti Bolognese")
        self.assertNotContains(response, "Grilled Cheese")

        response = self.client.get(reverse('recipe_list'), {'q': 'cheese'})
        self.assertContains(response, "Grilled Cheese")
        self.assertNotContains(response, "Spaghetti Bolognese")
