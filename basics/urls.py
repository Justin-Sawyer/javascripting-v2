from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.all_basics, name='basics'),
    path('<int:article_id>/', views.article, name='article_detail'),
    path('add/', views.add_article, name='add_article'),
]
