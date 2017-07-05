from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Programming, Framework

# Create your views here.
class ProgrammingList(ListView):
    template_name = 'programming_list.html'
    model = Programming
    paginate_by = 5