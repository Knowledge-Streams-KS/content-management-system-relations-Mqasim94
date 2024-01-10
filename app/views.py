# Views and Templates:

# Homepage: List of articles with titles and publication dates.
# Category Page: List of articles within a selected category.
# Article Detail Page: Full content of a selected article.
# Article Creation Form: A form for creating new articles, 
# associating them with categories and the author (user).
# Category Creation Form: A form for creating new categories.

from django.shortcuts import render
# Create your views here.

from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, Category, UserProfile
from .forms import ArticleForm, CategoryForm

def homepage(request):
    articles = Article.objects.all().order_by('-publication_date')
    return render(request, 'homepage.html', {'articles': articles})

def category_page(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    articles_in_category = category.article_set.all()
    return render(request, 'category_page.html', {'category': category, 'articles': articles_in_category})

def article_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'article_detail.html', {'article': article})

def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.save()
            form.save_m2m()  # Save many-to-many relationships
            return redirect('homepage')  # Redirect to homepage after article creation
    else:
        form = ArticleForm()
    return render(request, 'create_article.html', {'form': form})

def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save()
            return redirect('homepage')  # Redirect to homepage after category creation
    else:
        form = CategoryForm()
    return render(request, 'create_category.html', {'form': form})
