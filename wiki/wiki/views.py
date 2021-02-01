from django.shortcuts import render
import markdown2
from encyclopedia import util



def Django(request):
    return render(request, "encyclopedia/Django.html", {
        "entries": markdown2.markdown(util.get_entry('Django'))
    })

def CSS(request):
    return render(request, "encyclopedia/CSS.html", {
        "entries": markdown2.markdown(util.get_entry('CSS'))
    })

def Git(request):
    return render(request, "encyclopedia/Git.html", {
        "entries": markdown2.markdown(util.get_entry('Git'))
    })

def HTML(request):
    return render(request, "encyclopedia/HTML.html", {
        "entries": markdown2.markdown(util.get_entry('HTML'))
    })

def Python(request):
    return render(request, "encyclopedia/Python.html", {
        "entries": markdown2.markdown(util.get_entry('Python'))
    })