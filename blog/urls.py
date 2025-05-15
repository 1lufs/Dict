from django.urls import path
from . import views



urlpatterns = [

    path('', views.post_list, name='post_list'),
    path('word/<int:pk>/', views.post_list, name='word_detail'),
    path('word/new/', views.word_new, name='word_new'),
    path('word/<int:pk>/edit/', views.word_edit, name='word_edit')
]

