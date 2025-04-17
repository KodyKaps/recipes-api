from django.db import models

# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    ingredients = models.TextField(help_text="Comma-separated list of ingredients")
    cooking_time = models.IntegerField(help_text="Cooking time in minutes")
    difficulty = models.CharField(max_length=20, blank=True)
    image_url = models.URLField(blank=True, null=True)
    allergens = models.TextField(null = True)
    def calculate_difficulty(self):
        # Example logic: More ingredients or longer cooking time = higher difficulty
        num_ingredients = len(self.ingredients.split(","))
        if self.cooking_time < 10 and num_ingredients < 4:
            return "Easy"
        elif self.cooking_time < 20:
            return "Medium"
        else:
            return "Hard"

    def __str__(self):
        return self.name