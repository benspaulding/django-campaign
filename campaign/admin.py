# -*- coding: utf-8 -*-

"""
Django admin models for a campaign application.

"""

from django.contrib import admin

from campaign.models import Supporter, Entry, Issue

class EntryAdmin(admin.ModelAdmin):
    date_hierarchy = 'pub_date'
    fieldsets = (
        (u'Metadata', {'fields': (('title', 'slug'), 'subtitle', 'author', 'pub_date',)}),
        (u'Entry', {'fields': ('summary_txt', 'body_txt',)}),
        (u'Categorization', {'fields': ('tag_list', 'status',)}),
    )
    list_display = ('title', 'pub_date', 'author', 'status',)
    list_filter = ['pub_date', 'status']
    list_per_page = 50
    search_fields = ['title', 'subtitle', 'body_txt']
    prepopulated_fields = {'slug': ('title',)}

class IssueAdmin(admin.ModelAdmin):
    fieldsets = (
        (u'Metadata', {'fields': (('issue', 'slug',), 'ordering')}),
        (u'Position', {'fields': ('position_summary_txt', 'position_txt',)}),
        (u'Categorization', {'fields': ('tag_list', 'status',)}),
    )
    list_display = ('issue', 'ordering', 'tag_list', 'status',)
    list_filter = ['status']
    list_per_page = 50
    search_fields = ['issue', 'position_summary_txt', 'position_txt', 'tag_list']
    prepopulated_fields = {'slug': ('issue',)}

class SupporterAdmin(admin.ModelAdmin):
    date_hierarchy = 'submit_date'
    fieldsets = (
        (u'Supporter', {'fields': ('first_name', 'last_name', 'title', 'organization',)}),
        (u'Contact information', {'fields': (('address_1', 'address_2',), ('city', 'state',), ('country', 'zip_code',), 'email', 'phone',)}),
        (u'Supporting actions', {'fields': (('yard_sign', 'yard_sign_delivered',), ('poster', 'poster_delivered',), ('volunteer', 'contacted',), 'fundraising', 'support_list', 'donated', 'message',)}),
        (u'Meta', {'fields': ('submit_date', 'ip_address', 'status',)}),
    )
    list_display = ('__unicode__', 'email', 'yard_sign', 'poster', 'support_list', 'volunteer', 'fundraising', 'donated', 'contacted', 'status')
    list_filter = ['submit_date', 'status', 'yard_sign', 'yard_sign_delivered', 'poster', 'poster_delivered', 'support_list', 'volunteer', 'fundraising', 'donated', 'contacted']
    list_per_page = 100
    search_fields = ['first_name', 'last_name', 'address_1', 'message']

admin.site.register(Entry, EntryAdmin)
admin.site.register(Issue, IssueAdmin)
admin.site.register(Supporter, SupporterAdmin)
