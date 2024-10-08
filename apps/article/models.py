from django.db import models
from ckeditor.fields import RichTextField

from apps.course.models import Tag
from apps.user.models import Reaction, User


class Article(models.Model):
    """
        Статья
    """
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to="article/%Y/%m/%d", blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    content = RichTextField()

    is_published = models.BooleanField(default=False)

    views = models.ManyToManyField(User, related_name='articleViews', blank=True)
    reactions = models.ManyToManyField(Reaction,
                                       related_name='articleReactions',
                                       default=[],
                                       blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title


class ArticleComment(models.Model):
    """
        Комментарий к статье
    """
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField(max_length=600)

    likes = models.ManyToManyField(User, related_name='commentLikes', blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f"{self.article.title} - {self.user.username}"

