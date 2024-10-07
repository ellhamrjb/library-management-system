from django.urls import path
from . import views

urlpatterns = [
    path('borrowings/', views.BorrowingListCreateView.as_view(), name='borrowing-list-create'),
    path('borrowings/<int:pk>/', views.BorrowingDetailView.as_view(), name='borrowing-detail'),
    path('returns/', views.ReturnListCreateView.as_view(), name='return-list-create'),
    path('returns/<int:pk>/', views.ReturnDetailView.as_view(), name='return-detail'),
]
