from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from restaurant.forms import ajoutTypeRestaurantForm, ajoutRestaurantForm
from .models import Restaurant, TypeResto, Commentaire
from datetime import datetime, timedelta
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, View


class ajoutTypeRestaurant(CreateView):
  template_name = 'ajoutTypeRestaurant.html'
  form_class = ajoutTypeRestaurantForm

  def get_success_url(self):
      return reverse('accueil')

  def form_valid(self, form):
        form.save()
        return super().form_valid(form)

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context["txtBouton"] = 'Ajouter'
      return context

class ajoutRestaurant(CreateView):
  template_name = 'ajoutRestaurant.html'
  form_class = ajoutRestaurantForm

  def get_success_url(self):
      return reverse('accueil')

  def form_valid(self, form):
        form.save()
        return super().form_valid(form)

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context["txtBouton"] = 'Ajouter'
      return context