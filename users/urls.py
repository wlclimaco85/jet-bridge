from django import urls
from django.urls import path
from django.urls.conf import include


from . import views

app_name = "user"

urlpatterns = [
    path("",views.UserListView.as_view(), name="list"),
    path("<username:username>/",views.UserDetailView.as_view(), name="detail"),
]
