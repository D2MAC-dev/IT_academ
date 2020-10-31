from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

# Create your views here.

# def book_tabl(request):
#     return HttpResponse("Таблица врое как сделана, но на сервер не загрузилась, только GIDHUB")

"""Return list of Book objects"""

def show_book_list_view(request):
    books = Book.objects.all()
    con = {'books_key':books}
    return render(request, template_name="book_tabl/book_list.html", context=con) 
    

def show_book_by_pk_view(request, book_id):
    book_obj = Book.objects.get(pk=book_id)
    con = {'book':book_obj}
    return render(request, template_name="book_tabl/book.html", context=con) 
    