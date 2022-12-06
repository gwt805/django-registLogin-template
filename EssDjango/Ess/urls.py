from django.conf import settings
from django.urls import path, re_path
from django.views import static
from . import views

urlpatterns = [
    path('regist/', views.regist),
    path('login/', views.login),
    path('index/', views.index),
    path('nshowall', views.nei_showAll),
    re_path(
        "^static/(?P<path>.*)$",
        static.serve,
        {"document_root": settings.STATIC_ROOT},
        name="static",
    ),  # if debug is False
]
