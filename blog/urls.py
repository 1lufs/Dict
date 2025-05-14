from django.urls import path
from . import views
from .views import search_view
from .models import Word

urlpatterns = [
    
    path('search/', search_view, name='search'),
    path('', views.post_list, name='post_list'),
    path('word/<int:pk>/', views.post_list, name='word_detail'),
    path('word/new/', views.word_new, name='word_new'),
    path('word/<int:pk>/edit/', views.word_edit, name='word_edit')
]

