from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home_view(request, *args, **kwargs):
    # print(args, kwargs)
    print(request.user)
    # return HttpResponse("<h1>Hello World</h1>")  # string of html code
    return render(request, "home.html", {})


def contact_view(request, *args, **kwargs):
    print(request.user)
    return render(request, "contact.html", {})


def about_view(request, *args, **kwargs):
    print(request)
    my_context = {
        "title": "this is about us.",
        "my_number": 123,
        "my_list": [123, 456, 789],
        "my_html": "<h1>Hello World</h1>"

    }
    return render(request, "about.html", my_context)
