import datetime
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def hello_world(request: HttpRequest) -> HttpResponse:
    now = datetime.datetime.now()
    return HttpResponse("<html>"
                        "<h1>Hello, world!</h1>"
                        f"<h4>Current moment: {now}</h4>"
                        "<html>")


def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse("<h1>D'AZUR</h1>")
