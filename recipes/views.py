from django.shortcuts import render
from .models import Recipe
from django.db.models import Q

# Create your views here.
def recipe_list(request):
    query = request.GET.get('q')
    if query:
        recipes = Recipe.objects.filter(
            Q(name__icontains=query) | Q(ingredients__icontains=query)
        )
    else:
        #retreive from db
        recipes = Recipe.objects.all()
    return render(request, 'recipes/recipe_list.html', {
        'recipes': recipes,
        'query': query,
    })
