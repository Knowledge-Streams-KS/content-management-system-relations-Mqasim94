from django import forms
from .models import Article, Category

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'publication_date', 'categories']
        

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        
