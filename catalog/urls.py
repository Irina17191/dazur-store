from django.urls import path

from catalog.views import hello_world


urlpatterns = [
    path("hello-world/", hello_world, name="hello_world"),

]

app_name = "catalog"
