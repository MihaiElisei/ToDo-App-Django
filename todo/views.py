from django.shortcuts import render
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
    return render(request, 'todo/add_item.html')
