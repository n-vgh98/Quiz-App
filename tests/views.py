from django.http import HttpRequest
from django.shortcuts import render
from .models import Test
import random
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, '_base.html')


@login_required(login_url='/accounts/login')
def test(request):
    questions = Test.objects.filter(is_valid=True).order_by('?')[:5]
    if request.method == 'POST':
        print(request.POST)
        score = 0
        wrong = 0
        correct = 0
        no_answer = 0
        for q in questions:
            answer = q.answer
            question = request.POST.get(q.question)
            print(request.POST.get(q.question))
            print(q.answer)
            if answer == question:
                score += 10
                correct += 1
            elif question is None:
                no_answer += 1
            else:
                wrong += 1
        context = {
            'score': score,
            'correct': correct,
            'wrong': wrong,
            'no_answer': no_answer
        }
        return render(request, 'tests/total.html', context)
    else:
        context = {
            'questions': questions
        }
        return render(request, 'tests/test.html', context)
