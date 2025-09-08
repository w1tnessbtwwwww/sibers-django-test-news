from django.db import models
from django.urls import reverse
from django.utils import timezone

class News(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержание")
    pub_date = models.DateTimeField(default=timezone.now, verbose_name="Дата публикации")
    image = models.ImageField(upload_to='news_images/', blank=True, null=True, verbose_name="Изображение")
    
    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ['-pub_date']
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('news_detail', kwargs={'pk': self.pk})
    
