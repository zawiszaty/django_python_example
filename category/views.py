from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.template import RequestContext

from category.form import CategoryForm
from category.models import Category


def get_all(request):
    category = Category.objects.all()
    return render_to_response("categoreis/allCategories.html", {'categories': category})


def create_category(request):
    form = CategoryForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('get_all_categories')

    return render_to_response("categoreis/createCategory.html", {
        'form': form
    }, RequestContext(request))


def edit_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    form = CategoryForm(request.POST or None, instance=category)

    if form.is_valid():
        form.save()
        return redirect("get_all_categories")
    return render_to_response("categoreis/editCategory.html", {
        'category': category,
        'form': form
    }, RequestContext(request))


def delete_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    category.delete()
    return redirect('get_all_categories')