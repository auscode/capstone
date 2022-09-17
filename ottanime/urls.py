from django.urls import path
from . views import *

# here are my views

app_name = 'ottanime'


urlpatterns = [
    path("", Home.as_view(), name="Home"),
    path('accounts/profile/', ProfileList.as_view(), name="profile-list"),
    path('profiles/create/', ProfileCreate.as_view(), name="profile-create"),
    path('watch/<str:profile_id>/', MovieList.as_view(), name="movie-list"),
    path('watch/detail/<str:movie_id>/',
         MovieDetail.as_view(), name="movie-detail"),
    path('watch/play/<str:movie_id>/', PlayMovie.as_view(), name="play-movie"),
]


