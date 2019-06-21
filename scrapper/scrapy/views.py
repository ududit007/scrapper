from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic



class IndexView(generic.ListView):
    template_name = 'index.html'

def register(request):
    return render(request, 'register.html')







