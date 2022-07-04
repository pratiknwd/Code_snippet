from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from .forms import SavedDataForm
from .models import SavedData
from django.views.generic import ListView, DetailView

 # Create your views here.

# Create
def index(request):
	form = SavedDataForm()
	if request.method == 'POST':
		form = SavedDataForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	context = {'form':form, 'DB' : SavedData.objects.all()}
	return render(request, 'index.html', context)


# Viewing Data
def viewData(request,pk):
    return render(request, 'view.html',{
        'data' : SavedData.objects.get(id=pk)
    }) 


# Delete from DB
def deleteData(request,pk):
    data = SavedData.objects.get(id=pk)
    data.delete()
    return redirect('/')


#Update using my View
def edit(request, pk): 
    instance = SavedData.objects.get(id=pk)
    form = SavedDataForm(request.POST or None, instance=instance)
    if form.is_valid():
          form.save()
          return redirect('/')
    return render(request, 'update.html', {'form': form})  