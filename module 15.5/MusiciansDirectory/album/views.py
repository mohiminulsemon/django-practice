from django.shortcuts import render, redirect
from . import forms
from . import models
# Create your views here.


def album_list(request):
    albums = models.Album.objects.all()
    print(albums)
    return render(request, 'album_list.html', {'albums': albums})


def add_album(request):
    if request.method == 'POST':
        album_form = forms.AlbumForm(request.POST)
        if album_form.is_valid():
            album_form.save()
            return redirect('add_album')
    else:
        album_form = forms.AlbumForm()
    return render(request, 'add_album.html', {'form': album_form})

def edit_album(request, album_id):

    album = models.Album.objects.get(pk=album_id)

    if request.method == 'POST':
        album_form = forms.AlbumForm(request.POST, instance=album)
        if album_form.is_valid():
            album_form.save()
            return redirect('home')
    else:
        album_form = forms.AlbumForm(instance=album)

    return render(request, 'add_album.html', {'form': album_form})


def delete_album(request, album_id):
    album = models.Album.objects.get(pk=album_id)
    album.delete()
    return redirect('home')