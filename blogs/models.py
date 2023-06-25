from django.db import models

# Create your models here.

class Blog(models.Model):
    author = models.ForeignKey(to='auth.User', on_delete=models.CASCADE)
    title = models.CharField(verbose_name='Название', max_length=150)
    text = models.TextField(verbose_name='Контент',blank=True)
    image = models.ImageField(verbose_name='Изображение',blank=True)
    created_at = models.DateTimeField(verbose_name='Создано', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Изменено', auto_now=True)

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
        ordering = ['created_at', ]

    def __str__(self):
        return f'{self.title}'

    
