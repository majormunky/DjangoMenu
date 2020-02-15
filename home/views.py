from django.shortcuts import render
from home import models


def index(request):
    menu_items = models.MenuItem.objects.filter(parent__isnull=True)
    return render(request, "home/index.html", {"menu_items": menu_items})
