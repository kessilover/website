#-*-coding: utf-8 -*-
from datetime import datetime
from django.http import HttpResponse, Http404
from django.shortcuts import redirect, render, get_object_or_404
from .models import Story


def home(request):
    text = """<h1> Well hello there my dear friends</h1>  <p>how you do??</p>"""
    return HttpResponse(text)

def affichage(request, id):
    stories = get_object_or_404(Story, chapter=id)
    return render(request, 'stories/tlp.html', {'last_stories' : stories})