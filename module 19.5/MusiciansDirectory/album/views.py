from django.shortcuts import render, redirect
from . import forms
from . import models

from django.views.generic import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

from django.contrib.auth.mixins import UserPassesTestMixin

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

# class view

class EditAlbumUpdateView(UserPassesTestMixin,UpdateView):
    model = models.Album
    template_name = 'add_album.html'
    form_class = forms.AlbumForm
    success_url = reverse_lazy('profile')
    pk_url_kwarg = 'album_id'

    def test_func(self):
        return self.request.user.is_authenticated

    def handle_no_permission(self):
        return redirect('login')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    


class AddAlbumCreateView(UserPassesTestMixin,CreateView):
    model = models.Album
    template_name = 'add_album.html'
    form_class = forms.AlbumForm
    success_url = reverse_lazy('profile')

    def test_func(self):    
        return self.request.user.is_authenticated

    def handle_no_permission(self):    
        return redirect('login')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class DeleteAlbumView(DeleteView):
    model = models.Album
    template_name = 'delete_album.html'
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'album_id'