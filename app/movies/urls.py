from django.urls import include, path
from rest_framework import routers  # ,serializers, viewsets

# from .views import MovieList, MovieDetail
from movies import views as movie_views

router = routers.SimpleRouter()
router.register(prefix=r"movies", viewset=movie_views.MovieViewSet)

urlpatterns = [
    path("api/", include(router.urls))
    # path('api/movies/', MovieList.as_view()),
    # path("api/movies/<int:pk>/", MovieDetail.as_view()),
]
