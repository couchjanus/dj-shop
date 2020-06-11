from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache

# Create your views here.

# Serve Vue Application
index = never_cache(TemplateView.as_view(template_name='index.html'))
