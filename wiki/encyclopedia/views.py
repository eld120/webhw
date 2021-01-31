from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def Django(request):
    return render(request, "encyclopedia/Django.html", {
        "entries": util.get_entry('Django')
    })

def CSS(request):
    return render(request, "encyclopedia/CSS.html", {
        "entries": util.get_entry('CSS')
    })

def Git(request):
    return render(request, "encyclopedia/Git.html", {
        "entries": util.get_entry('Git')
    })

def HTML(request):
    return render(request, "encyclopedia/HTML.html", {
        "entries": util.get_entry('HTML')
    })

def Python(request):
    return render(request, "encyclopedia/Python.html", {
        "entries": util.get_entry('Python')
    })