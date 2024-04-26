from django.http import HttpResponse, HttpResponseRedirect
from .models import Question
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
def index(request):
    questions = Question.objects.order_by('question_text')
    context = {'questions': questions}
    return render(request, 'enquete/index.html', context)
