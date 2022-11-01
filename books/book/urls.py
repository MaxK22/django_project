from django.urls import path

from . import views

app_name = 'book'
urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='book_list'),
    path('authors/', views.AuthorListView.as_view(), name='author_list'),
    path('book/<int:pk>/', views.BookDetailView.as_view(), name='book_info'),
    path('author/<int:pk>/', views.AuthorDetailView.as_view(), name='author_info'),
    path('author/create/', views.AuthorCreateView.as_view(), name='create_author'),
    path('author/<int:pk>/update/', views.AuthorUpdateView.as_view(), name='update_author'),
    path('author/<int:pk>/delete/', views.AuthorDeleteView.as_view(), name='delete_author'),
    path('book/create/', views.BookCreateView.as_view(), name='create_book'),
    path('book/<int:pk>/update/', views.BookUpdateView.as_view(), name='update_book'),
    path('book/<int:pk>/delete/', views.BookDeleteView.as_view(), name='delete_book'),
]