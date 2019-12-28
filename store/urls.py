from django.conf.urls import url
from .views import view_books

urlpatterns = [
    url(r'^$', view_books),
]
