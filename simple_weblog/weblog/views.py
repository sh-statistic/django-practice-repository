from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Article, Comment


# Create your views here.
def get_article_list(request):
    articles = Article.objects.all()
    data = [{'id': article.id, 'title': article.title} for article in articles]
    return JsonResponse(data, safe=False)


def get_article_details(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    data = {'id': article.id, 'title': article.title, 'content': article.content}
    return JsonResponse(data)


def filter_articles_by_topic(request, topic):
    articles = Article.objects.filter(topic=topic)
    data = [{'id': article.id, 'title': article.title} for article in articles]
    return JsonResponse(data, safe=False)


def post_comment(request, article_id):
    if request.method == 'POST':
        article = get_object_or_404(Article, pk=article_id)
        text = request.POST.get('text', '')
        author = request.POST.get('author', '')
        Comment.objects.create(article=article, text=text, author=author)
        return JsonResponse({'message': 'Comment posted successfully'})
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
