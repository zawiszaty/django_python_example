from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('authors/', include('authors.urls')),
    path('book/', include('books.urls')),
    path('admin/', admin.site.urls),
    path('category/', include('category.urls')),
    path('', include('home.urls'))
]
