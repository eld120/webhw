from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.fields import DateTimeField, IntegerField


class User(AbstractUser):
    cash = models.IntegerField(default=1000, null=True)
    my_bids = models.ForeignKey("auctions.Bids",  on_delete=models.CASCADE, null=True)
    my_comments = models.ForeignKey("auctions.Comments",  on_delete=models.CASCADE, null=True)


class Listings(models.Model):
    title = models.CharField(max_length=150, null=True)
    description = models.TextField(max_length=500, null=True)
    #add img URL to schema
    active = models.BooleanField(default=True, null=True)
    start_price = models.IntegerField(null=True)
    end_price = models.IntegerField(blank=True, null=True)
    auction_length = models.DateTimeField(null=True)
    auction_start = models.DateTimeField(auto_now=True, null=True)
    auction_end = models.DateTimeField(auto_now=True, null=True)
    auction_winner = models.ForeignKey("auctions.User" , null=True, on_delete=models.CASCADE)

class Bids(models.Model):
    
    bid_amount = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(auto_now=True, null=True)
    current_bid = models.IntegerField(blank=True, null=True)
    winning_bid = models.BooleanField(blank=True, null=True)
    contact_id = models.ForeignKey("auctions.User" , null=True, on_delete=models.CASCADE)
    listing_id = models.ForeignKey( "auctions.Listings" , null=True, on_delete=models.CASCADE)


class Comments(models.Model):
    listing_bid = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(auto_now=True, auto_now_add=False, null=True)
    current_bid = models.IntegerField(blank=True, null=True)
    winning_bid = models.BooleanField(blank=True, null=True)
    contact_id = models.ForeignKey("auctions.User" , null=True, on_delete=models.CASCADE)
    listing_id = models.ForeignKey( "auctions.Listings" , null=True, on_delete=models.CASCADE)