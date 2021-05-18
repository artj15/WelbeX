'''from django.shortcuts import render
from .models import Table, TableFrom
# Create your views here.
def TableView(request):
    table = Table.objects.all()
    data = {
        'table': table
    }
    return render(request, 'table.html', context= data)'''
from django_tables2 import  SingleTableMixin
from django_filters.views import FilterView
from .models import Table
from .tables import MyTable

class WelView(SingleTableMixin, FilterView):
    model = Table
    table_class = MyTable
    template_name = 'table.html'
    filterset_fields = ['data', 'name', 'number', 'distance']
