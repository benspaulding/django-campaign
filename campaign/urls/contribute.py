# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *
from django.views.generic import create_update, list_detail, simple
from django.core.urlresolvers import reverse

from campaign.models import Supporter


info_dict = {
    'queryset': Supporter.public.all(),
}


urlpatterns = patterns('',

    url(r'^supporters/added/$', 
                        simple.direct_to_template, 
                        {
                            'template': 'campaign/supporter_added.html',
                        }, 
                        name='campaign_supporter_added'),
        
    url(r'^supporters/$', 
                        list_detail.object_list, 
                        dict(
                            info_dict, 
                            template_name='campaign/supporter_list.html', 
                            template_object_name='supporter', 
                            ), 
                        name='campaign_supporter_list'),
        
    url(r'^donate/success/$', 
                        simple.direct_to_template, 
                        {
                            'template': 'campaign/donate_success.html',
                        }, 
                        name='campaign_donate_success'),
        
    url(r'^donate/$', 
                        create_update.create_object, 
                        {
                            'model': Supporter, 
                            'post_save_redirect': 'donate/success/',#reverse('campaign_donate_success'), 
                            'template_name': 'campaign/donate_form.html', 
                        }, 
                        name='campaign_donate_form'),
        
    url(r'^$',  
                        create_update.create_object, 
                        {
                            'model': Supporter, 
                            'post_save_redirect': 'supporters/added/',#reverse('campaign_supporter_added'), 
                            'template_name': 'campaign/contribute_index.html', 
                        }, 
                        name='campaign_supporter_form'),
)