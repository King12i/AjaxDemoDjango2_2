from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('snakes/all', views.allSnakes),
    path('snakes/new', views.snakeForm),
    path('snakes/add', views.addSnake),
    path('snakes/<int:snake_id>', views.oneSnake),
    path('snakes/<int:snake_id>/delete', views.deleteSnake)
]