import debug_toolbar
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import include
from django.urls import path

from .views import index

urlpatterns = [
    path("", login_required(index), name="index"),
    path("admin/", admin.site.urls),
    path("__debug__/", include(debug_toolbar.urls)),
]
