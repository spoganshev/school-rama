'''
Created on May 14, 2012

@author: spoganshev
'''
from django.http import Http404
from django.shortcuts import render_to_response

def hello_world(request, parameter):
    try:
        number = int(parameter)
    except ValueError:
        raise Http404()
    return render_to_response('test.html', locals())
