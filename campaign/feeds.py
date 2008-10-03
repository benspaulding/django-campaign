# -*- coding: utf-8 -*-

import datetime

from django.contrib.syndication.feeds import Feed
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse

from campaign.models import *


CURRENT_SITE = Site.objects.get_current()


class CampaignEntryFeed(Feed):

    description = u'Latest journal entries from the campaign trail.'
    
    def title(self):
        return u'%s / Campaign Journal' % CURRENT_SITE.name
    
    def link(self):
        return u'http://%s%s' % (CURRENT_SITE.domain, reverse('campaign_entry_archive_index'))
    
    def author_name(self):
        return u'Adam Stout'
    
    def item_author_name(self, item):
        return u'Adam Stout'
    
    def author_link(self):
        return u'http://%s/%s/' % (CURRENT_SITE.domain, u'about')
    
    def copyright(self):
        return u'Copyright 2007 Adam Stout. All rights reserved.'

    def items(self):
        return Entry.public.all()[:10]



class CampaignIssueFeed(Feed):

    description = u'Rexburg issues and Adam\'s position.'
    
    def title(self):
        return u'%s / On the Issues' % CURRENT_SITE.name
    
    def link(self):
        return u'http://%s%s' % (CURRENT_SITE.domain, reverse('campaign_issue_list'))
    
    def author_name(self):
        return u'Adam Stout'
    
    def item_author_name(self, item):
        return u'Adam Stout'
    
    def author_link(self):
        return u'http://%s/%s/' % (CURRENT_SITE.domain, u'about')
    
    def copyright(self):
        return u'Copyright 2007 Adam Stout. All rights reserved.'

    def items(self):
        return Issue.public.all()