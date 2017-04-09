from django.shortcuts import render
from django.http import HttpResponse
from .forms import AddForm
# Create your views here.

def index(request):
    if request.method == "POST":
        form = AddForm(request.POST)
        print form,"form------------"

        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
    else:
        form = AddForm()
    return  render(request,"form.html",{"form":form})



