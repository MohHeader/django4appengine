# -*- coding: utf-8 -*-
""" The password_required decorator for Django views """
from functools import update_wrapper, wraps
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.utils.decorators import available_attrs
from django.utils.http import urlquote
from django.conf import settings

import sys
def stagingServer(request):
    if request.META['HTTP_HOST'] in settings.STAGING_SERVER_URLS:
        return True
    else:
        return False

def friendClient(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    if ip in settings.FRIENDS_IPS:
        return True
    else:
        return False

def password_required(view_func=None, redirect_field_name=REDIRECT_FIELD_NAME):
    """
    Decorator for views that checks that the user has entered the password,
    redirecting to the log-in page if necessary.
    """
    def _wrapped_view(request, *args, **kwargs):
        if not stagingServer(request):
            return view_func(request, *args, **kwargs)
        else:
            if friendClient(request):
                return view_func(request, *args, **kwargs)
            elif request.session.get('password_required_auth', False):
                return view_func(request, *args, **kwargs)

        return HttpResponseRedirect('%s?%s=%s' % (
            reverse('libs.password_required.views.login'),
            redirect_field_name,
            urlquote(request.get_full_path()),
        ))
    return wraps(view_func, assigned=available_attrs(view_func))(_wrapped_view)