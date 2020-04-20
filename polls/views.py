from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse
from .models import Question
from django.template import loader
# Create your views here.


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    try:
        question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    return HttpResponse("you are looking at the result of question %s." % question_id)


def vote(request, question_id):
    return HttpResponse("you are voting on the question %s." % question_id)