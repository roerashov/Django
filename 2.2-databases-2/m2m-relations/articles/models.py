from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название тэга')

    class Meta:
        verbose_name = "Наименование тэгов"
        verbose_name_plural = "Наименование тэгов"

    def __str__(self):
        return self.name



class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    scopes = models.ManyToManyField(Tag, through='Scopes', through_fields=('title','name'))

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title
    
    
class Scopes(models.Model):
    title = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scopes1')
    name = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='scopes1') 
    is_main = models.BooleanField(verbose_name='Основной')
    
    class Meta:
        verbose_name = 'Связки тэгов'
        
   

