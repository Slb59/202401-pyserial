"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from . import views

handler404 = "config.views.page_not_found"
handler500 = "config.views.server_error"

urlpatterns = [
    path("", views.index, name="index"),
    path("admin/", admin.site.urls),
]


if settings.DEBUG:
    # This allows the error pages to be debugged during development.
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
        path(
            "404/",
            views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", views.server_error),
    ]
