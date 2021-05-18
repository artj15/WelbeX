import  django_tables2 as tables
from .models import Table
class MyTable(tables.Table):
    data = tables.Column(orderable=False)
    class Meta:
        model = Table
        fields = ('data', 'name', 'number', 'distance')
