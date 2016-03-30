# -*- coding: utf-8 -*-
import sys
import json

#from django
from django.conf import settings
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.template import Context, RequestContext
from django.http import HttpResponse, HttpResponseRedirect

def landing_page(request):
    return render_to_response('landing_page.html',locals(),context_instance = RequestContext(request))

def home(request):
    try:
        request.session.delete_test_cookie()
    except:
        pass
    request.session.set_test_cookie()
    request.session['session_check'] = "This is from new session text, after 2.45pm"
    return render_to_response('home.html',locals(),context_instance = RequestContext(request))
    
    

def remove_session(request):
    if 'session_check' in request.session: 
        del request.session['session_check']
    return HttpResponseRedirect(reverse('landing_page',))
