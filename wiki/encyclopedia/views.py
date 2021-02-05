from django.http.response import HttpResponseNotFound
from django.shortcuts import render
import markdown2
from . import util
from django.http import Http404

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

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




def search(request):
    if request.method == 'GET':
        
        srch =  request.GET.get('q', None).lower()
        
        #returns a list of all entries in lowercase for easier matching
        links = util.list_entries()
        links_lowercase = [x.lower() for x in links]
        
        try:
            indx = links_lowercase.index(srch)

            return render(request, ('encyclopedia/'+ links[indx] + '.html'), {
                "entries" :  markdown2.markdown(util.get_entry(links[indx]))
            })
        except ValueError:
            raise Http404(' Entry not found')
            

        