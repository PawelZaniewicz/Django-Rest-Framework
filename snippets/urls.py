from django.urls import path
from snippets import views

urlpatterns = [
    path("snippets/", views.SnippetList.as_view()),
    path("snippets/<int:pk>", views.SnippetDetails.as_view()),

    path("users/", views.UserList.as_view()),
    path("users/<int:pk>", views.UserDetails.as_view())

]