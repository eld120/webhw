from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic.detail import DetailView
from .forms import ListingCreateForm
from .models import Listing, User
from django.views.generic import ListView, CreateView, DeleteView, UpdateView


class IndexView(ListView):
    model = Listing
    template_name = 'auctions/index.html'
    context_object_name = 'context'
    
# def index(request):
#     return render(request, "auctions/index.html")


class ListingDetail(DetailView):
    model = Listing
    template_name = 'auctions/listing_detail.html'
    

class ListingCreate(CreateView):
    model = Listing
    template_name = 'auctions/listing_create.html'
    form_class = ListingCreateForm
    #fields = [ 'title', 'image', 'description', 'active', 'start_price', 'auction_length', 'slug']
    success_url = reverse_lazy('index')


class ListingDelete(DeleteView):
    model = Listing
    template_name = "auctions/listing_create.html"
    form_class = ListingCreateForm
    success_url = reverse_lazy('index')

class ListingUpdate(UpdateView):
    template_name = "auctions/listing_create.html"
    queryset = Listing.objects.all()
    form_class = ListingCreateForm

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
