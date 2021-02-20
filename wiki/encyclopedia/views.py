from django.http.response import HttpResponseNotFound
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
import markdown2
from . import util
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):

    return render(request, "encyclopedia/entry.html", {
        "entries": markdown2.markdown(util.get_entry(title)),
        "md_name": title
    })

def edit(request, title):

    if request.method == "POST":
        editwiki = {
            'md_name' : title,
            'content' : request.POST['editwiki']        
            }
        util.save_entry(editwiki['md_name'], editwiki['content'])
        return render(request, 'encyclopedia/newpage.html', {
                'errors' : 'Successful wiki entry updated'
            })
    return render(request, 'encyclopedia/edit.html', {
            "md_name" : title ,
            "contents" : util.get_entry(title)
            })
    '''return reverse("edit", kwargs={"title": title})'''

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
            #list to keep track of matching substrings
            sub_inx = []
            ret_inx = []

            for link in links_lowercase:
                if srch in link:
                    sub_inx.append(links_lowercase.index(link))
                
            for inx in sub_inx:
                ret_inx.append(links[inx])
                
            #needs to display a list of all encyclopedia entries that have the query as a substring
            return render(request, "encyclopedia/index.html", {
        "entries": ret_inx
    })

@csrf_exempt
def newpage(request):

    if request.method == "POST":
        newwiki = {
            'title' : request.POST['newtitle'],
            'content' : request.POST['newwiki']        
            }

        if newwiki['title'] in util.list_entries():
            return render(request, 'encyclopedia/newpage.html', {
                'errors' : 'Error duplicate page found'
            })
        else:
            util.save_entry(newwiki['title'], newwiki['content'])
            return render(request, 'encyclopedia/newpage.html', {
                'errors' : 'Successful wiki entry created'
            })

    return render(request, 'encyclopedia/newpage.html', {
        'errors' : None
    })

