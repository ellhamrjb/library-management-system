from django.contrib import admin
from django.urls import path,include
from users.views import login_view, signup_view, logout_view, welcome_page,welcome_page
from books.views import category_list_view, book_list_view
from borrowing.views import borrow_list_view, return_list_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/books/', include('books.urls')),
    path('api/borrowing/', include('borrowing.urls')),
    path('api/reviews/', include('reviews.urls')),
    path('', welcome_page, name='welcome'),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('logout/', logout_view, name='logout'),
    path('categories/', category_list_view, name='category-list'),
    path('books/', book_list_view, name='book-list'),
    path('borrowings/', borrow_list_view, name='borrow-list'),
    path('returns/', return_list_view, name='return-list'),
]
