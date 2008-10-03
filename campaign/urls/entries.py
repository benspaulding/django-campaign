# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *
from django.views.generic import date_based

from campaign.models import Entry


info_dict = {
    'queryset': Entry.public.all(),
    'date_field': 'pub_date',
}


urlpatterns = patterns('',
    url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/(?P<slug>[-\w]+)/$', 
        date_based.object_detail, 
        dict(info_dict, slug_field='slug', template_object_name='entry'), 
        name='campaign_entry_detail'),
    url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/$', 
        date_based.archive_day, 
        dict(info_dict, template_object_name='entry'), 
        name='campaign_entry_archive_day'),
    url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/$', 
        date_based.archive_month, 
        dict(info_dict, template_object_name='entry'),
        name='campaign_entry_archive_month'),
    url(r'^(?P<year>\d{4})/$', 
        date_based.archive_year, 
        dict(info_dict, make_object_list=True, template_object_name='entry'), 
        name='campaign_entry_archive_year'),
    url(r'^$', 
        date_based.archive_index, 
        info_dict, 
        name='campaign_entry_archive_index'),
)