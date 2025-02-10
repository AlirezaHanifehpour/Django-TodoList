from django.urls import path
from .views import * 

app_name = 'todo_app'

urlpatterns = [
    path('',HomeView.as_view(),name="home"),
    path('remove_book/<int:book_id>/',remove_book,name='remove_book'),
    path('clear-book/',clear_book,name='clear_book')
]