from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.template import RequestContext

from books.form import BookForm
from books.models import Books


def get_all(request):
    books = Books.objects.all()
    return render_to_response("books/booksAll.html", {'books': books})


def create_book(request):
    form = BookForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('get_all_book')

    return render_to_response("books/createBook.html", {
        'form': form
    }, RequestContext(request))


def edit_book(request, book_id):
    books = get_object_or_404(Books, pk=book_id)
    form = BookForm(request.POST or None, instance=books)

    if form.is_valid():
        form.save()
        return redirect("get_all_book")
    return render_to_response("books/editBook.html", {
        'books': books,
        'form': form
    }, RequestContext(request))


def delete_book(request, book_id):
    books = get_object_or_404(Books, pk=book_id)
    books.delete()

    return redirect('get_all_book')
