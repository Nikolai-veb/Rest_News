from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListArticleView.as_view()),
    path('article/<slug:slug>/', views.DetailArticleView.as_view()),
    path('add_article/', views.CreateArticleView.as_view()),
    path('update_article/<slug:slug>/', views.UpdateArticleView.as_view()),
    path('delete_article/<slug:slug>/', views.DeleteArticleView.as_view()),
]