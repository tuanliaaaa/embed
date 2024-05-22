from django.urls import path
from .views import Home,Handle
urlpatterns = [
   path('',Home.as_view()),
   path("handle",Handle.as_view())
]
