from django.urls import path

from . import views

urlpatterns = [
    path('', views.all_basics, name='basics'),
    path('<article_id>', views.article, name='article_detail'),
]
