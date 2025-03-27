"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
from .models import Comment
from .models import Blog
from taggit.forms import TagWidget

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Логин'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Пароль'}))

class FeedbackForm(forms.Form):
    name = forms.CharField(label="Ваше имя", max_length=100, required=True)
    email = forms.EmailField(label="Электронная почта", required=True)
    rating = forms.ChoiceField(
        label="Оцените сайт", 
        choices=[(1, '1 - Плохо'), (2, '2'), (3, '3'), (4, '4'), (5, '5 - Отлично')],
        widget=forms.RadioSelect
    )
    topics = forms.MultipleChoiceField(
        label="Что вам понравилось на сайте?",
        choices=[('design', 'Дизайн'), ('content', 'Контент'), ('usability', 'Удобство')],
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    suggestions = forms.CharField(
        label="Ваши предложения",
        widget=forms.Textarea,
        required=False,
        max_length=1000
    )

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        labels = {'text': "Комментарий"}
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Введите ваш комментарий...'}),
        }

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'description', 'content', 'image', 'tags'] 
        labels = {
            'title': 'Заголовок',
            'description': 'Краткое описание',
            'content': 'Полное содержание',
            'image': 'Изображение поста',
            'tags': 'Теги',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 6}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'tags': TagWidget(attrs={'class': 'form-control', 'placeholder': 'технологии, искусственный интеллект'}),
        }