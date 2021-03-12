from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.db.models.fields import DateTimeField, IntegerField, SlugField


class User(AbstractUser):
    cash = models.IntegerField(default=1000, null=True)
    my_bids = models.ForeignKey("auctions.Bid",  on_delete=models.CASCADE, null=True)
    my_comments = models.ForeignKey("auctions.Comment",  on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.first_name + self.last_name

class Listing(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=150, null=True)
    description = models.TextField(max_length=500, null=True)
    image = models.URLField(max_length=350, null=True, blank=True)
    active = models.BooleanField(default=True, null=True)
    start_price = models.FloatField(null=True)
    end_price = models.FloatField(blank=True, null=True)
    auction_length = models.DateTimeField(null=True)
    auction_start = models.DateTimeField(auto_now=True, null=True)
    auction_end = models.DateTimeField(auto_now=True, null=True, blank=True)
    auction_winner = models.ForeignKey("auctions.User" ,blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return 'Listing title: ' + self.title

    def get_absolute_url(self):
        
        return reverse("listing_detail", kwargs={'slug' : self.slug})
    

class Bid(models.Model):
    slug = models.SlugField(null=True)
    bid_amount = models.FloatField(blank=True, null=True)
    date = models.DateTimeField(auto_now=True, null=True)
    current_bid = models.FloatField(blank=True, null=True)
    winning_bid = models.BooleanField(blank=True, null=True)
    contact_id = models.ForeignKey("auctions.User" , null=True, on_delete=models.CASCADE)
    listing_id = models.ForeignKey( "auctions.Listing" , null=True, on_delete=models.CASCADE)

    
    def __str__(self):
        return 'Contact ID: ' + str(self.contact_id) + 'Listing ID: ' + str(self.listing_id)

    def get_absolute_url(self):
        return reverse("Bid", kwargs={'slug':self.slug})
    

class Comment(models.Model):
    slug = models.SlugField(null=True)
    text = models.TextField(max_length=500)
    comment_date = models.DateTimeField(auto_now=True, null=True)
    contact_id = models.ForeignKey("auctions.User" , null=True, on_delete=models.CASCADE)
    listing_id = models.ForeignKey( "auctions.Listing" , null=True, on_delete=models.CASCADE)

    def __str__(self):
        return 'Contact ID: ' + str(self.contact_id) + 'Listing ID: ' + str(self.listing_id) + str(self.comment_date)
    
    def get_absolute_url(self):
        return reverse("Comment", kwargs={'slug':self.slug})
    