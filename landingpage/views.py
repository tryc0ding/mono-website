from django.http import HttpResponse
from django.template.response import TemplateResponse


def index(request):
    response = TemplateResponse(request, "index.html", {})
    return response
