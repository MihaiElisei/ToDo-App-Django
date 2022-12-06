from django.shortcuts import render, redirect
from .models import Item

# Create your views here.


def get_todo_list(request):
    # query set for all items in the model
    items = Item.objects.all()
    # a dictionary with all items 
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)


def add_item(request):
    # create an item in database
    if request.method == "POST":
        name = request.POST.get('item_name')
        done = 'done' in request.POST
        Item.objects.create(name=name, done=done)
        return redirect('get_todo_list')
    return render(request, 'todo/add_item.html')
