from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from neighbor.forms import FoodForm, NeighborCreationForm
from django.utils.text import slugify

def become_neighbor(request):
    if request.method == 'POST':
        form = NeighborCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect('core:home')
    else:
        form = NeighborCreationForm()

    return render(request, 'neighbor/become_neighbor.html', {'form': form})


@login_required
def add_food(request):
    if request.method == 'POST':
        form = FoodForm(request.POST, request.FILES)

        if form.is_valid():
            print("form valid")
            food = form.save(commit=False) # Because we have not given neighbor yet
            food.neighbor = request.user.neighbor

            food.slug = slugify(food.title)
            food.save() #finally save

            return redirect('core:home')

    else:
        form = FoodForm

    return render(request, 'neighbor/add_food.html', {'form': form})