from django.urls import path
from .views import login, UserCreate


urlpatterns = [
    path('login/', login),
    path('signup/', UserCreate.as_view()),
]


