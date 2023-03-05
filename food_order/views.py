from django.shortcuts import render
from food_order.forms import FoodOrderForm
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.utils.text import slugify
from food.models import Food


# Create your views here.
def order_food(request, food_id):
    if request.method == 'POST':
        form = FoodOrderForm(request.POST, request.FILES)

        if form.is_valid():
            print("form valid")
            food_order = form.save(commit=False) # Because we have not given neighbor yet
            food_order.ordered_by = request.user.neighbor
            food_order.food = Food.objects.get(id=food_id)

            print(food_order)
            print(food_order)

            food_order.save() #finally save

            return redirect('core:home')

    else:
        form = FoodOrderForm

    return render(request, 'food_order/food_order.html', {'form': form})