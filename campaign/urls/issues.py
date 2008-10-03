# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *
from django.views.generic import list_detail

from campaign.models import Issue


info_dict = {
    'queryset': Issue.public.all(),
}


urlpatterns = patterns('',
    url(r'^(?P<slug>[-\w]+)/$', 
        list_detail.object_detail, 
        dict(info_dict, slug_field='slug', template_object_name='issue'), 
        name='campaign_issue_detail'),
    url(r'^$', 
        list_detail.object_list, 
        dict(info_dict, template_object_name='issue'), 
        name='campaign_issue_list'),
)