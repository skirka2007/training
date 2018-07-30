from django.shortcuts import render
from qa.models import Question, Answer
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.core.paginator import Paginator 

# Create your views here.
def index(request):
    try:
        page=int(request.GET.get("page"))
    except ValueError:
        page = 1
    except TypeError:
        page = 1    
    questions = Question.objects.new() #May be mistake here - wrong ordering or wrong declaration of method new
    paginator = Paginator(questions, 10)
    page = paginator.page(page)
    return render(request, 'templates/list_questions.html', {
        'questions': page.object_list,
        'title': 'The latest', #May be mistake here
        'paginator': paginator,
        'page': page,
    })

def popular(request):
    try:
        page=int(request.GET.get("page"))
    except ValueError:
        page = 1
    except TypeError:
        page = 1    
    questions = Question.objects.popular() #May be mistake here - wrong ordering or wrong declaration of method popular
    paginator = Paginator(questions, 10)
    page = paginator.page(page)
    return render(request, 'templates/list_questions.html', {
        'questions': page.object_list,
        'title': 'Popular', #May be mistake here
        'paginator': paginator,
        'page': page,
    })

def question_page(request, pk):
    try:
        quest = Question.objects.get(id=pk)
    except Question.DoesNotExist:
        raise Http404for answer in question.answer_set.all 
    ans = Answer.objects.filter(question_id = pk) #May be mistake, in this case just use question.answer_set.all 
    return render(request, 'templates/question_with_answer.html', {
        'question': quest,
        'answers': ans,
    })

def test(request, *args, **kwargs):
    return HttpResponse('OK')




