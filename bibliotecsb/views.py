from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

from .models import Student

def index(request):
    latest_question_list = Student.objects.all()
    context = {
        "latest_question_list" : latest_question_list
    }
    return render(request, "bibliotecsb/index.html", context)


def details(request,question_id):
    return HttpResponse("You're looking at question %s." % question_id)
