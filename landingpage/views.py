from django.template.response import TemplateResponse
from django.shortcuts import render

def index(request):
    response = TemplateResponse(request, "index.html", {})
    return response

def impressum(request):
    response = TemplateResponse(request, "impressum.html", {})
    return response

def index(request):
    return render(request, "index.html")