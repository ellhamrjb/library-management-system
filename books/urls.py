from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
    path('authors/', views.AuthorListCreateView.as_view(), name='author-list-create'),
    path('authors/<int:pk>/', views.AuthorDetailView.as_view(), name='author-detail'),
    path('publishers/', views.PublisherListCreateView.as_view(), name='publisher-list-create'),
    path('publishers/<int:pk>/', views.PublisherDetailView.as_view(), name='publisher-detail'),
    path('genres/', views.GenreListCreateView.as_view(), name='genre-list-create'),
    path('genres/<int:pk>/', views.GenreDetailView.as_view(), name='genre-detail'),
]
