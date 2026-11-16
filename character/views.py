from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# test view
def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse('These are your PCs.')