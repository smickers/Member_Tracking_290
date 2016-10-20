from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template("contact_log.html")
    context = {
        "message": "hello world"
    }
    return HttpResponse(template.render(context, request))