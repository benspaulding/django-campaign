# -*- coding: utf-8 -*-

import datetime

from django.views.generic.create_update import *

from campaign.models import Supporter

def supporter_add(request, model, post_save_redirect, template_name,):
    return create_object(request, qmodel, post_save_redirect, template_name,)