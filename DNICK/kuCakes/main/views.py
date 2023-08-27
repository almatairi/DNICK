from django.shortcuts import render , redirect , get_object_or_404
from django.urls import reverse

from .models import Cake, OrderedCakes
from .forms import CakeForm

def index(request):
    
    cakes = Cake.objects.all()

    context = {
        'cakes':cakes
    }
    return render(request , 'index.html', context)

def orderCakeForm(request, pk):
    cake = Cake.objects.get(id=pk)

    if request.method == 'POST':
        form = CakeForm(request.POST, request.FILES, instance=cake)
        if form.is_valid():
            form.save()
            ordered_cake, created = OrderedCakes.objects.get_or_create(cake=cake)
            ordered_cake.occasion = form.cleaned_data['occasion']
            ordered_cake.servingSize = form.cleaned_data['servingSize']
            ordered_cake.flavor = form.cleaned_data['flavor']
            ordered_cake.toppings = form.cleaned_data['toppings']
            ordered_cake.cardMessage = form.cleaned_data['cardMessage']

            ordered_cake.name = cake.name
            ordered_cake.description = cake.description
            ordered_cake.image = cake.image
            ordered_cake.price = cake.price

            ordered_cake.save()
            
            return redirect('final' , cake.id)

    else:
        form = CakeForm(instance=cake)

    context = {
        'form': form,
        'cake': cake
    }
    return render(request, 'orderCake.html', context)

def finalStage(request , pk):
    cake = OrderedCakes.objects.get(id=pk)

    context = {
        'cake':cake
    }

    return render(request , 'finalStage.html' , context)
