# Content Management System (CMS) for Articles and Categories
# Models:

# Articles Model: Fields include title, content, publication_date. 
# Establish a Many-to-Many relationship with categories.
# Categories Model: Fields include name. Each category can be associated with multiple articles.
# User Model: (For Many-to-One) Include fields like username, email, password. 
# Each user can create multiple articles.



from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    publication_date = models.DateTimeField()
    categories = models.ManyToManyField(Category)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    





# from django.db import models
# # Create your models here.
    
# class Category_Model(models.Model):
#     name = models.CharField(max_length = 64)

#     def __str__(self):
#         return self.name

# class User_Model(models.Model):
#     u_name = models.CharField(max_length = 64)
#     u_email = models.EmailField
#     u_paw = models.CharField(max_length = 16)

#     def __str__(self):
#         return self.u_name

# class Artical_Model(models.Model):
#     titel = models.CharField(max_length = 64)
#     content = models.CharField(max_length = 64)
#     p_date = models.DateTimeField(auto_now=True, auto_now_add=True)
#     category = models.ManyToManyField(Category_Model)
#     author = models.name = models.ForeignKey('User_Model', on_delete=models.CASCADE)
#     def __str__(self):
#         return self.titel