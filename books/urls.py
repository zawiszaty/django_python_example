from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_all, name='get_all_book'),
    path('add', views.create_book, name='create_book'),
    path('edit/<int:book_id>', views.edit_book, name='edit_book'),
    path('delete/<int:book_id>', views.delete_book, name='delete_book')
]
