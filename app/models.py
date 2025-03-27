from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime
from taggit.managers import TaggableManager


class Blog(models.Model):
    title = models.CharField(
        max_length=100,
        unique_for_date="posted",
        verbose_name="Заголовок"
    )
    slug = models.SlugField(
        max_length=100,
        unique=True,
        verbose_name="Слаг (URL-идентификатор)"
    )
    author = models.ForeignKey(
        User,

        on_delete=models.CASCADE,
        verbose_name="Автор"
    )
    description = models.TextField(
        verbose_name="Краткое содержание"
    )
    content = models.TextField(
        verbose_name="Полное содержание"
    )
    posted = models.DateTimeField(
        default=datetime.now,
        db_index=True,
        verbose_name="Опубликована"
    )

    tags = TaggableManager(verbose_name="Теги", blank=True)
    image = models.ImageField(upload_to="blog_images/", default="blog_images/temp.jpg", blank=True)

    def get_absolute_url(self):
        return reverse("blogpost", args=[str(self.id)])

    def __str__(self):
        return f"{self.title} — {self.author.username}"

    class Meta:
        db_table = "Posts"
        ordering = ["-posted"]
        verbose_name = "статья блога"
        verbose_name_plural = "статьи блога"


# Настройки административного отображения
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "posted", "slug")
    list_filter = ("posted", "author", "tags")
    search_fields = ("title", "content", "author__username", "tags__name")
    prepopulated_fields = {"slug": ("title",)}
    date_hierarchy = "posted"

class Comment(models.Model):
    text = models.TextField("Комментарий")
    date = models.DateTimeField("Дата добавления", default=datetime.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    post = models.ForeignKey("Blog", on_delete=models.CASCADE, verbose_name="Статья")

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"Комментарий от {self.author} к посту '{self.post.title}'"

