from django.shortcuts import render,get_object_or_404

from .models import *

def index(request):

    context = {
        'department': Department.objects.all()

    }
    return render(request, 'index.html', context)

def student( request, sid):
    context = {
    'student': get_object_or_404(Student, pk=sid)
    }

    return render(request, "student.html", context)