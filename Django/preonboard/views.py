

# Create your views here.
from django.shortcuts import render
from .models import Job_opening


def index(request):
    question_list = Job_opening.objects.order_by('-create_date')
    context = {'question_list': question_list}
    return render(request, 'pybo/question_list.html', context)