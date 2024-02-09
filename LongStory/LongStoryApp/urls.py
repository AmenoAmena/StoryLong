from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("story/", views.story_show, name = "story"),
    path('contribute/', views.contribute, name='contribute')
]