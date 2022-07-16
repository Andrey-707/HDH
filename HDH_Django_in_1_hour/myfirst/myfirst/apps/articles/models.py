import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Article(models.Model):
	"""
	Статья.
	"""
	article_title = models.CharField('Название статьи.', max_length=200)
	article_text = models.TextField('Текст статьи.')
	publish_date = models.DateTimeField('Дата публикации.')

	def __str__(self):
		return f'{self.article_title}'

	def was_published_recently(self):
		"""
		Метод указывает на то, была ли статья опубликована недавно.
		"""
		published_recently = self.publish_date >= (timezone.now() - datetime.timedelta(7))
		return 'Статья опубликована недавно.' if published_recently else 'Статья опубликована давно.'

	class Meta:
		verbose_name = 'Статья'
		verbose_name_plural = 'Статья'


class Comment(models.Model):
	"""
	Комментарий.
	"""
	article = models.ForeignKey(Article, on_delete=models.CASCADE)
	author_name = models.CharField('Имя автора.', max_length=50)
	comment_text = models.CharField('Текст комментария.', max_length=200)

	def __str__(self):
		return f'{self.author_name}'

	class Meta:
		verbose_name = 'Комментарий'
		verbose_name_plural = 'Комментарии'
