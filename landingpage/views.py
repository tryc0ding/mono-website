from django.template.response import TemplateResponse


def index(request):
    response = TemplateResponse(request, "index.html", {})
    return response
def impressum(request):
    response = TemplateResponse(request, "impressum.html", {})
    return response