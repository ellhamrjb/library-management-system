from django.urls import path
from . import views

urlpatterns = [
    path('reviews/', views.ReviewListCreateView.as_view(), name='review-list-create'),
    path('reviews/<int:pk>/', views.ReviewDetailView.as_view(), name='review-detail'),
    path('ratings/', views.RatingListCreateView.as_view(), name='rating-list-create'),
    path('ratings/<int:pk>/', views.RatingDetailView.as_view(), name='rating-detail'),
]
