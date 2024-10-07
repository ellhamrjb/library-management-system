from django.urls import path
from . import views
from .views import signup_view, login_view, logout_view

urlpatterns = [
    path('profiles/', views.ProfileListCreateView.as_view(), name='profile-list-create'),
    path('profiles/<int:pk>/', views.ProfileDetailView.as_view(), name='profile-detail'),
    path('roles/', views.RoleListCreateView.as_view(), name='role-list-create'),
    path('roles/<int:pk>/', views.RoleDetailView.as_view(), name='role-detail'),
    path('memberships/', views.MembershipListCreateView.as_view(), name='membership-list-create'),
    path('memberships/<int:pk>/', views.MembershipDetailView.as_view(), name='membership-detail'),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('logout/', logout_view, name='logout'),
]
