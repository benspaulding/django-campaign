# -*- coding: utf-8 -*-

from django import forms
from django.core.validators import alnum_re
from django.contrib.localflavor.us.forms import *

from campaign.models import Supporter, TITLE_CHOICES


# I put this on all required fields, because it's easier to pick up
# on them with CSS or JavaScript if they have a class of "required"
# in the HTML. Your mileage may vary. If/when Django ticket #3515
# lands in trunk, this will no longer be necessary.
attrs_dict = { 'class': 'required' }


class SupporterForm(forms.Form):
    """
    
    
    """
    
    # Supporter
    first_name = forms.CharField(max_length=32, widget=forms.TextInput(attrs=attrs_dict),)
    last_name = forms.CharField(max_length=64, widget=forms.TextInput(attrs=attrs_dict),)
    title = forms.ChoiceField(choices=TITLE_CHOICES, required=False,)
    organization = forms.CharField(max_length=64, required=False,)
    
    # Contact info
    address_1 = forms.CharField(max_length=100, required=False,)
    address_2 = forms.CharField(max_length=100, required=False,)
    city = forms.CharField(max_length=100, widget=forms.TextInput(attrs=attrs_dict),)
    state = USStateField(widget=forms.TextInput(attrs=attrs_dict),)
    country = forms.CharField(max_length=100, widget=forms.TextInput(attrs=attrs_dict),)
    zip_code = USZipCodeField(widget=forms.TextInput(attrs=attrs_dict),)
    email = forms.EmailField(widget=forms.TextInput(attrs=attrs_dict),)
    phone = USPhoneNumberField(required=False,)
    
    # Supporting actions
    message = forms.CharField(widget=forms.Textarea, required=False,)
    support_list = forms.BooleanField(required=False,)
    yard_sign = forms.BooleanField(required=False,)
    poster = forms.BooleanField(required=False,)
    volunteer = forms.BooleanField(required=False,)
    fundraising = forms.BooleanField(required=False,)
    donated = forms.BooleanField(required=False,)
    
    # Follow-up
    contacted = forms.BooleanField()
    yard_sign_delivered = forms.BooleanField()
    poster_delivered = forms.BooleanField()
    
    # Meta
    ip_address = forms.IPAddressField()
    submit_date = forms.DateTimeField()
    status = forms.IntegerField()