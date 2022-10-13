from django.urls import path
from . import views

urlpatterns=[
    path('hello/', views.HelloView.as_view()),
    path('musicians/', views.MusicianView.as_view())
]