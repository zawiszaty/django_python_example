from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_all, name='get_all_categories'),
    path('add', views.create_category, name='create_category'),
    path('edit/<int:category_id>', views.edit_category, name='edit_category'),
    path('delete/<int:category_id>', views.delete_category, name='delete_category'),
]
