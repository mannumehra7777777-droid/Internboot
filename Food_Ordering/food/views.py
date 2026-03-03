
# Create your views here.
from .models import FoodItem
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            login(request, user) # Automatically log them in after signup
            return redirect('menu') # Redirect to your menu page
    else:
        form = UserCreationForm()
    return render(request, 'food/signup.html', {'form': form})

@login_required(login_url='login')
def menu_page(request):
    all_food = FoodItem.objects.all() 
    return render(request, 'food/menu.html', {'items': all_food})