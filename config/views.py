from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def page_not_found(request, exception):
    response = render(request, "base/404.html", {})
    response.status_code = 404
    return response


def server_error(request, exception=None):
    response = render(request, "base/500.html", {})
    response.status_code = 500
    return response
