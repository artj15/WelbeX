from django.shortcuts import render
from .models import Table


# Create your views here.
def TableView(request):
    table = Table.objects.all()
    data = {
        'table': table
    }
    return render(request, 'table.html', context=data)
