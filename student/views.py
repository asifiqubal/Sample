
from django.http import HttpResponse
from django.template import loader

from .models import *

def index(request):

    template = loader.get_template('index.html')
    context = {
        'department': Department.objects.all()

    }
    return HttpResponse(template.render(context, request))

def student(request, sid):
    template = loader.get_template('student.html')
    context = {
        'student': Student.objects.get(id=sid)
    }
    return HttpResponse(template.render(context, request))