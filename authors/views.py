from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from authors.form import AuthorForm
from authors.models import Author


def get_all(request):
    authors = Author.objects.all()
    return render_to_response("authors/authorall.html", {'authors': authors})


def create_author(request):
    form = AuthorForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('get_all_authors')

    return render_to_response("authors/createAuthor.html", {
        'form': form
    }, RequestContext(request))


def edit_author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    form = AuthorForm(request.POST or None, instance=author)

    if form.is_valid():
        form.save()
        return redirect("get_all_authors")
    return render_to_response("authors/editAuthor.html", {
        'author': author,
        'form': form
    }, RequestContext(request))


def delete_author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    author.delete()

    return redirect("get_all_authors")
