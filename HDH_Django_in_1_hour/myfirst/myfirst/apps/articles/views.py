from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Article


# Create your views here.
def index(request):
	"""
	My view nemed idnex.
	"""
	# срез списка из пяти элементов, отсортированного реверсивоно (минусовая сортировка)
	latest_article_list = Article.objects.order_by('-publish_date')[:5]
	
	return render(request, 'articles/list1.html', {'latest_article_list': latest_article_list})


def detail(request, article_id):
	"""
	My view nemed detail.
	"""
	try:
		a = Article.objects.get(id=article_id)
	except Exception:
		raise  Http404('Статья не найдена.')

	latest_comments_list = a.comment_set.order_by('-id')[:10]

	return render(request, 'articles/detail.html', {'article': a, 'latest_comments_list': latest_comments_list})


def leave_comment(request, article_id):
	"""
	My view nemed leave_comment.
	"""
	try:
		a = Article.objects.get(id=article_id)
	except Exception:
		raise  Http404('Статья не найдена.')

	a.comment_set.create(author_name=request.POST['name'], comment_text=request.POST['text'])
	
	return HttpResponseRedirect(reverse('articles:detail', args=(a.id,)))


def test(request):
	"""
	My view nemed test.
	"""
	return render(request, 'articles/list2.html')
