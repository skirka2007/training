from django.shortcuts import render
from qa.models import Question, Answer
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.core.paginator import Paginator 
from qa.forms import AskForm, AnswerForm, LoginForm, SignupForm
from django.contrib.auth import authenticate, login

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
            form.author = request.user
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
            quest.author = request.user
            url = quest.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'add_ask.html', {
        'form': form
    })

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {
        'form': form,
        'user': request.user,
        'session': request.session,
    })


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
    else:
        form = LoginForm()
    return render(request, 'login.html', {
        'form': form,
        'user': request.user,
        'session': request.session,
    })    

def test(request, *args, **kwargs):
    return HttpResponse('OK')




