from django.db import models
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Snack

# Create your views here.
class HomeListView(ListView):
    template_name= 'snacks/list.html'
    model = Snack
class DetailsListView(DetailView):
    template_name = 'snacks/details.html'
    model = Snack
class CreateListView(CreateView):
    template_name = 'snacks/create.html'
    model = Snack
    fields = ["title","purcheser","description"]
class UpdateListView(UpdateView):
    template_name = 'snacks/update.html'
    model = Snack
    fields = ["title","purcheser","description"]
class DeleteListView(DeleteView):
    template_name = 'snacks/delete.html'
    model = Snack
    success_url = reverse_lazy("list")