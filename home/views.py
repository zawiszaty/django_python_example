from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect, get_object_or_404

from authors.models import Author


def index(request):
    return render_to_response("index.html")
