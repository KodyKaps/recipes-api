from django.shortcuts import render
from .models import Recipe
from django.db.models import Q

# Create your views here.
#home landing page
def landing_page(request):
    return render(request, 'landing.html')

#recipes list
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


