from django.shortcuts import render, redirect
from .models import Recipe
from django.db.models import Q

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

import matplotlib.pyplot as plt
from io import BytesIO
import base64
# Create your views here.
#home landing page
def landing_page(request):
    return render(request, 'landing.html')


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')  # redirect to homepage or dashboard
        else:
            messages.error(request, "Invalid username or password")
    
    return render(request, 'accounts/login.html')

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, "Passwords do not match")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
        else:
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            return redirect('/')
    
    return render(request, 'accounts/register.html')

def logout_view(request):
    logout(request)
    return redirect('login')

#recipes list
@login_required
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

@login_required
def reviews(request):

    # 🔹 Mock data (e.g., recipe names and number of reviews)
    labels = ['Pasta', 'Tacos', 'Pizza', 'Sushi', 'Salad']
    data = [15, 25, 35, 10, 15]  # number of reviews per recipe

    # 🔸 Create the pie chart
    fig, ax = plt.subplots()
    ax.pie(data, labels=labels, autopct='%1.1f%%', startangle=140)
    ax.axis('equal')

    # 🔸 Save to buffer
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    chart = base64.b64encode(image_png).decode('utf-8')

    return render(request, 'recipes/reviews.html',{'chart': chart})