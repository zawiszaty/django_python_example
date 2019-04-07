from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_all, name='get_all_authors'),
    path('author', views.create_author, name='create_author'),
    path('author/<int:author_id>', views.edit_author, name='edit_author'),
    path('author/delete/<int:author_id>', views.delete_author, name='delete_author'),
]
