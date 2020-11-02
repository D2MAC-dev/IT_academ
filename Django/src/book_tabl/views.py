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
    

def create_new_book(request):
    # name = request.POST.get('name')
    # genre = request.POST.get('genre')
    # author = request.POST.get('author')
    # publisher = request.POST.get('publisher')
    # isbn = request.POST.get('isbn')
    # price = request.POST.get('price')
    # amount = request.POST.get('amount')

    # Book.objects.create(book_name=name, book_genres=genre, book_author=author, 
    #                     book_publisher=publisher, isbn_code=isbn, book_price=price,
    #                     books_amount=amount
    #                     )
    return render(request, template_name="book_tabl/create_new_book.html", context={})
