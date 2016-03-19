from django.shortcuts import render
from django.template import loader
# Create your views here.
from django.http import HttpResponse

from models import *

def topic_list(request):
    topics = Topic.objects.all()
    template = loader.get_template('list.html')

    return HttpResponse(template.render(locals(),request))

def topic_detail(request, topic_id):
    print topic_id
    students = Student.objects.all()
    sessions = Session.objects.all()
    topic = Topic.objects.get(pk=topic_id)
    template = loader.get_template('detail.html')
    return HttpResponse(template.render(locals(),request))


