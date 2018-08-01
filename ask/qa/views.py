from django.shortcuts import render
from qa.models import Question, Answer
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.core.paginator import Paginator 
from qa.forms import AskForm, AnswerForm

# Create your views here.
def index(request):
    try:
        page=int(request.GET.get("page"))
    except ValueError:
        page = 1
    except TypeError:
        page = 1    
    questions = Question.objects.new() 
    paginator = Paginator(questions, 10)
    page = paginator.page(page)
    return render(request, 'list_questions.html', {
        'questions': page.object_list,
        'title': 'The latest', 
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
    questions = Question.objects.popular() 
    paginator = Paginator(questions, 10)
    page = paginator.page(page)
    return render(request, 'list_questions.html', {
        'questions': page.object_list,
        'title': 'Popular', 
        'paginator': paginator,
        'page': page,
    })

def question_page(request, pk):
    try:
        quest = Question.objects.get(id=pk)
    except Question.DoesNotExist:
        raise Http404
    ans = Answer.objects.filter(question_id = pk)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            form.save()
            url = quest.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AnswerForm(initial={'question': quest.id})
    return render(request, 'question_with_answers.html', {
        'question': quest,
        'answers': ans,
        'form' : form,
    })

def ask(request):
    if request.method == "POST":
        form = AskForm(request.POST)
        if form.is_valid():
            quest = form.save()
            url = quest.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'add_ask.html', {
        'form': form
    })
    

def test(request, *args, **kwargs):
    return HttpResponse('OK')




