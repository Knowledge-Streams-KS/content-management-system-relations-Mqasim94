from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.homepage, name='homepage'),
    path('category/<int:category_id>/', views.category_page, name='category_page'),
    path('article/<int:article_id>/', views.article_detail, name='article_detail'),
    path('create_article/', views.create_article, name='create_article'),
    path('create_category/', views.create_category, name='create_category'),
]

