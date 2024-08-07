from django.forms import ModelForm, CheckboxSelectMultiple

from apps.article.models import Article


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'image', 'content', 'tags', 'is_published')
        widgets = {
            'tags': CheckboxSelectMultiple,
        }


