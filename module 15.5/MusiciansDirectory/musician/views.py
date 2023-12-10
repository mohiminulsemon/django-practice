from django.shortcuts import render, redirect
from . import forms
from . import models
# Create your views here.


def musician_list(request):
    musicians = models.Musician.objects.all()
    print(musicians)
    return render(request, 'musician_list.html', {'musicians': musicians})

def add_musician(request):
    if request.method == 'POST':
        musician_form = forms.MusicianForm(request.POST)
        if musician_form.is_valid():
            musician_form.save()
            return redirect('add_musician')
    else:
        musician_form = forms.MusicianForm()
    return render(request, 'add_musician.html', {'form': musician_form})


def edit_musician(request, musician_id):

    musician = models.Musician.objects.get(pk=musician_id)

    if request.method == 'POST':
        musician_form = forms.MusicianForm(request.POST, instance=musician)
        if musician_form.is_valid():
            musician_form.save()
            return redirect('home')
    else:
        musician_form = forms.MusicianForm(instance=musician)

    return render(request, 'add_musician.html', {'form': musician_form})