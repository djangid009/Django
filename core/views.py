from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import Blog, Rank, Comment, Question, Answer
from .forms import BlogForm, QuestionForm, AnswerForm, CommentForm
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.db.models import F


def home_page(request):
    return render(request, 'index.html')


def questiondetails(request):
    form = QuestionForm()
    question = Question.objects.all()
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = QuestionForm(request.POST or None)
        if form.is_valid():
            questiontitle = form.cleaned_data.get('questiontitle')
            questiondetails = form.cleaned_data.get('questiondetails')
            question = Question(questiontitle=questiontitle,
                                questiondetails=questiondetails)
            question.save()
        else:
            print('Error')
    return render(request, 'questiondetails.html', context)


def question(request):
    question = Question.objets.all()[0]
    answer = Answer.objects.all()
    comment = Comment.objects.all()
    context = {
        'question': question,
        'answer': answer,
        'comment': comment
    }
    if request.method == 'POST':
        form = QuestionForm(request.POST or None)
        if form.is_valid():
            username = request.user.username
            questiontitle = form.cleaned_data.get('questiontitle')
            questiondetails = form.cleaned_data.get('questiondetails')
            question = question(
                username=username, questiontitle=questiontitle, questiondetails=questiondetails)
            question.save()
        else:
            print('Error')
    return render(request, 'question.html', context)


def log_out(request):
    logout(request)
    return redirect('/')


def profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    # return render(request, 'accounts/profile.html', args)
    blog = Blog.objects.filter(username=request.user.username)
    question = Question.objects.filter(username=request.user.username)
    user = request.user
    context = {
        'blog': blog,
        'user': user,
        'question': question
    }
    return render(request, 'profile.html', context)


def blog(request):
    form = BlogForm()
    user = request.user.username
    blog = Blog.objects.all()
    rank = Rank.objects.filter(name=request.user.username)
    context = {
        'form': form,
        'blog': blog
    }
    if request.method == 'POST':
        form = BlogForm(request.POST or None)
        if form.is_valid():
            username = user
            title = form.cleaned_data.get('title')
            message = form.cleaned_data.get('message')
            blogs = Blog(username=username, title=title, message=message)
            blogs.save()
            rank.update(points=F('points') + 10)
            #  return redirect('/')
        else:
            print('Error')
            # message = request.POST.get('message', '')
            # blogs = Blog(title=title, message=message)
            # blogs.save()
            # return redirect('')
            # return render(request, 'blog.html',{'blog': blog})
            # items_json = request.POST.get('itemsJson', '')
        # thank = True
        # id = order.order_id
        #  return render(request, 'blog.html',{'blog': blog})
    return render(request, 'blog.html', context)


def rank(request):
    rank_value = Rank.objects.all()
    return render(request, 'rank.html', {'rank_value': rank_value})

# def profile_info(request):
#     profile_value = Profile_info.objects.all()[0]
#     print('######')
#     print(profile_value)
#     return render(request, 'profile.html',{'profile_value': profile_value})
