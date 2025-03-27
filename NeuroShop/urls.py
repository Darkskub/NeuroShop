"""
Definition of urls for NeuroShop.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('admin/', admin.site.urls),
    path('links/', views.links, name='links'),
    path('pool/', views.pool, name='pool'),
    path('registration/', views. registration, name= 'registration'),
        path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Вход',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
     path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
     path('admin/', views.admin, name="admin"),
     path('blog/', views.blog, name='blog'),
     path('blog/tag/<slug:tag_slug>/', views.blog, name='blog_by_tag'),
     path('blogpost/<int:parametr>/', views.blogpost, name='blogpost'),
     path('newpost/', views.newpost, name='newpost'),
     path('video/', views.videopost, name='videopost'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
