"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from .forms import FeedbackForm
from django.contrib.auth.forms import UserCreationForm
from taggit.models import Tag
from .models import Blog
from .models import Comment
from .forms import CommentForm
from .forms import BlogForm
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from app.models import Blog
from django.core.paginator import Paginator

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Главная',
            'year':datetime.now().year,
        }
    )

def about(request):
    return render(request, 'app/about.html')

def contact(request):
    return render(request, 'app/contact.html')

def links(request):
    return render(request, 'app/links.html')

def pool(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            return render(request, 'app/pool.html', {
                'form': None,
                'data': data,
                'title': 'Спасибо за отзыв!',
            })
    else:
        form = FeedbackForm()

    return render(request, 'app/pool.html', {
        'form': form,
        'title': 'Обратная связь',
    })

def registration(request):
    """Отображает страницу регистрации."""

    if request.method == "POST":  # после отправки формы
        regform = UserCreationForm(request.POST)
        if regform.is_valid():
            reg_f = regform.save(commit=False)
            reg_f.is_staff = False                  # запрещен вход в административный раздел
            reg_f.is_active = True                  # активный пользователь
            reg_f.is_superuser = False              # не является суперпользователем
            reg_f.date_joined = datetime.now()      # дата регистрации
            reg_f.last_login = datetime.now()       # дата последней авторизации

            reg_f.save()                            # сохраняем изменения после добавления полей
            return redirect('home')                 # перенаправление на главную страницу после регистрации
    else:
        regform = UserCreationForm()                # создание объекта формы для ввода данных

    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/registration.html',
        {
            'regform': regform,                     # передача формы в шаблон веб-страницы
            'year': datetime.now().year,
        }
    )

def logout(request):
    logout(request)
    return redirect('login')

def admin(request):
    return redirect('admin')

def blog(request, tag_slug=None):
    posts = Blog.objects.all().order_by('-posted')
    tag = None

    if tag_slug:
        tag = Tag.objects.get(slug=tag_slug)
        posts = posts.filter(tags=tag)

    paginator = Paginator(posts, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'app/blog.html', {
        'posts': page_obj,
        'tag': tag,
        'title': 'Блог',
        'year': datetime.now().year,
    })


def blogpost(request, parametr):
    """Renders the blogpost page."""
    assert isinstance(request, HttpRequest)

    post_1 = Blog.objects.get(id=parametr)
    comments = Comment.objects.filter(post=parametr)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_f = form.save(commit=False)
            comment_f.author = request.user
            comment_f.date = datetime.now()
            comment_f.post = Blog.objects.get(id=parametr)
            comment_f.save()
        return redirect('blogpost', parametr=post_1.id)
    else:
        form = CommentForm()
    return render(
        request,
        'app/blogpost.html',
        {
            'post_1': post_1,
            'year': datetime.now().year,
            'comments': comments,
            'form': form,
        }
    )

def videopost(request):
    return render(request, 'app/videopost.html', {
        'title': 'Видео',
        'year': datetime.now().year,
    })

@login_required
def newpost(request):
    if not request.user.is_superuser:
        return redirect('home')

    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.posted = datetime.now()
            post.author = request.user

            base_slug = slugify(post.title)
            slug = base_slug
            counter = 1
            while Blog.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            post.slug = slug

            post.save()
            return redirect('blog')
    else:
        form = BlogForm()

    return render(request, 'app/newpost.html', {
        'form': form,
        'title': 'Новый пост',
        'year': datetime.now().year,
    })


