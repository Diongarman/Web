from django.views import generic
#Whenever you want to make a form to create/update/delete a new object import the below
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
#below authentic module takes usrname and password and verifies they are in the DB and login module attaches a session id so don't have to login on every page on site
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .models import Album
from .forms import UserForm

class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()

class DetailsView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'

class AlbumCreate(CreateView):
    #What type of object we creating?
    model = Album
    #what fields do we need the users to fill out?
    fields = ['artist', 'album_title', 'genre', 'album_logo']

class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']

class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')

class UserFormView(View):
    #what blue print are you using for your form
    form_class = UserForm
    template_name = 'music/registration_form.html'
    #display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})
    #process for data
    def post(self, request):
        #UserForm will validate this POST data
        form = self.form_class(request.POST)

        if form.is_valid():
            #doesn't save to DB yet
            user = form.save(commit=False)

            #cleaned (normalised) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            #returns User objects if credentials are correct
            #Below does this by checking is the arguments passed are in the DB
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('music:index')

        return render(request, self.template_name, {'form': form})


