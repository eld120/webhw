from django import forms
from django.forms.models import ModelForm
from django.views.generic.edit import CreateView
from .models import Listing, Bid, Comment


class ListingCreateForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = [ 'title', 'description', 'active', 'start_price', 'auction_length', 'slug']
    

# class ListingForm(ModelForm):
#     class Meta:
#         model = Listing
#         fields = [ 'title', 'description', 'active', 'start_price', 'auction_length']

    # title = forms.CharField(title='Title', max_length=150)
    # description = forms.Textarea(max_length=500)
    # start_price = forms.IntegerField()
    # auction_length = forms.DateTimeField()

# class BidForm(ModelForm):
#     class Meta:
#         model = Bid
#         fields = ['listing_id', 'listing_bid']

# class CommentForm(ModelForm):
#     class Meta:
#         model = Comment
#         fields = ['listing_id', 'text']