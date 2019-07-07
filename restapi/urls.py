from django.urls import include, path, re_path
from restapi.v1.authentication.views import LoginView, LogoutView

urlpatterns = [
    path('login', LoginView.as_view()),
    path('logout', LogoutView.as_view()),
]