from django.shortcuts import HttpResponseRedirect
from django.urls import reverse


def Index(request):
    return HttpResponseRedirect(reverse('App_Blog:blog_list'))