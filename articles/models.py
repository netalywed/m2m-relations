from django.db import models


class Scope(models.Model):
    name = models.CharField(max_length=100, verbose_name='Раздел')

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'



class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение', )
    scopes = models.ManyToManyField(Scope, related_name='articles', through='ArticleScope')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class ArticleScope(models.Model):
    scope = models.ForeignKey(Scope, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True)
    is_main = models.BooleanField(verbose_name='Основной')

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'
