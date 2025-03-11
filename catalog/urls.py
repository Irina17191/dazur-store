from django.urls import path

from catalog.views import hello_world, index

urlpatterns = [
    path("hello-world/", hello_world, name="hello_world"),
    path("", index, name="index"),

]

app_name = "catalog"
