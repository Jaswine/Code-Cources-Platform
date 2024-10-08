
from apps.article.forms import ArticleForm
from apps.article.models import Article
from apps.user.models import User


def create_article(form: ArticleForm, user: User) -> Article | None:
    """
        Создание статьи

        :param form: ArticleForm  - Заполненая форма статьи
        :param user: User         - Пользователь
        :return Article | None    - Статья или None
    """
    if form.is_valid():
        article = form.save(commit=False)
        article.user = user
        article.save()
        return article
    return None


def update_article(form: ArticleForm) -> Article | None:
    """
        Обновление статьи

        :param form: ArticleForm  - Заполненая форма статьи
        :return Article | None    - Статья или None
    """
    if form.is_valid():
        article = form.save()
        return article
    return None


def delete_article(article: Article):
    """
        Удаление статьи

        :param article: Article  - статья
    """
    article.delete()
