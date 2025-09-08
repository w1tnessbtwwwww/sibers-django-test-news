# newspaper/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from .models import News
from .forms import NewsForm

def news_list(request):
    # Получаем параметр paginate_by из GET запроса
    paginate_by = request.GET.get('paginate_by', 10)
    
    # Валидация значения
    if paginate_by not in ['10', '20', '50']:
        paginate_by = 10
    else:
        paginate_by = int(paginate_by)
    
    # Получаем все новости
    news_list = News.objects.all()
    
    # Пагинация
    paginator = Paginator(news_list, paginate_by)
    page = request.GET.get('page')
    
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)
    
    context = {
        'news': news,
        'paginate_by': paginate_by,
    }
    
    return render(request, 'newspaper/news_list.html', context)

def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            news = form.save()
            messages.success(request, 'Новость успешно добавлена!')
            return redirect('news_list')
    else:
        form = NewsForm()
    
    return render(request, 'newspaper/add_news.html', {'form': form})

def news_detail(request, pk):
    news = get_object_or_404(News, pk=pk)
    return render(request, 'newspaper/news_detail.html', {'news': news})