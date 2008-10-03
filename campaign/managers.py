# -*- coding: utf-8 -*-

from django.db import models


class PublicItemManager(models.Manager):
    """
    Custom manager for the Entry and Issue models, providing 
    shortcuts for filtering by item status.
    
    """
            
    def get_query_set(self):
        """
        Overrides the default ``QuerySet`` to only include Items
        with a status of 'public'.
        
        """
        return super(PublicItemManager, self).get_query_set().filter(status__exact=1)


class PublicSupporterManager(models.Manager):
    """
    Custom manager for the Supporter model, providing 
    shortcuts for filtering by item status.
    
    """
            
    def get_query_set(self):
        """
        Overrides the default ``QuerySet`` to only include Supporter
        with a status of 'public' and support_list of True.
        
        """
        return super(PublicSupporterManager, self).get_query_set().filter(status__exact=1).filter(support_list__exact=True)