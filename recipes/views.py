from django.shortcuts import render

# Create your views here.
def recipe_list(request):
    return render(request, 'recipes/recipe_list.html')