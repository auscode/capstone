from django.views import View
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from . forms import *
from . models import *


class Home(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('ottanime:profile-list')
        return render(request, 'index.html')


method_decorator(login_required, name='dispatch')


class ProfileList(View):
    def get(self, request, *args, **kwargs):
        # it gets the logged in user (request.user)
        profiles = request.user.profiles.all()
        # passing temp to context of profile list
        context = {
            'profiles': profiles
        }
        return render(request, 'profilelist.html', context)


method_decorator(login_required, name='dispatch')


class ProfileCreate(View):
    # get method decorator
    def get(self, request, *args, **kwargs):
        form = ProfileForm()
        context = {
            'form': form
        }
        return render(request, 'profilecreate.html', context)

    # post method decorator
    def post(self, request, *args, **kwargs):
        form = ProfileForm(request.POST or None)
        #
        if form.is_valid():
            # creating the profile form if is_valid usr
            profile = Profile.objects.create(**form.cleaned_data)
            # checking if usr has profile
            if profile:
                # if exixt create a option to add another profile
                request.user.profiles.add(profile)
                return redirect('ottanime:profile-list')
        context = {
            'form': form
        }
        return render(request, 'profilecreate.html', context)


method_decorator(login_required, name='dispatch')


class MovieList(View):
    def get(self, request, profile_id, *args, **kwargs):
        try:
            #getting obj of profile in profile
            profile = Profile.objects.get(uuid=profile_id)
            #getting the movies & filtering the movies with age limit
            movies = Movie.objects.filter(age_limit=profile.age_limit)
            # checkng the profile is logged in via the req usr
            if profile not in request.user.profiles.all():
                return redirect('ottanime:profile-list')
            context = {
                'movies': movies
            }
            return render(request, 'movielist.html', context)
        #if profile is not exist
        except Profile.DoesNotExist:
            return redirect('ottanime:profile-list')


method_decorator(login_required, name='dispatch')


class MovieDetail(View):
    def get(self, request, movie_id, *args, **kwargs):
        try:
            #getting movire acc. to uuid from request usr
            movie = Movie.objects.get(uuid=movie_id)

            context = {
                'movie': movie
            }

            return render(request, 'moviedetail.html', context)
        except Movie.DoesNotExist:
            return redirect('ottanime:profile-list')


method_decorator(login_required, name='dispatch')


class PlayMovie(View):
    def get(self, request, movie_id, *args, **kwargs):
        try:
            movie = Movie.objects.get(uuid=movie_id)
            movie = movie.video.values()

            context = {
                'movie': list(movie)#because we have more than one movie
            }

            return render(request, 'playmovie.html', context)
        except Movie.DoesNotExist:
            return redirect('ottanime:profile-list')
