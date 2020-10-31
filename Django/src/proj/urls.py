"""proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from hello_world.views import hello_world
from book_tabl.views import show_book_list_view, show_book_by_pk_view, create_new_book

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello-world', hello_world),
    path('book/<int:book_id>', show_book_by_pk_view),
    path('book/create/', create_new_book),
    path('', show_book_list_view),   
]
