from django.db import models
from datetime import date
from django.contrib.auth.models import User
# Create your models here.


class Department(models.Model):
    deptCode = models.CharField(max_length=5)
    deptName = models.CharField(max_length=100)
    isActive = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.deptCode}"
    
class News_volume_issue(models.Model):
    volume = models.IntegerField(default=1)
    issue = models.IntegerField(default=1)
    month_year = models.DateField(null=True, verbose_name='Date of publication', default=date.today)
    deptId = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    isActive = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.volume} ({self.issue})"

class Category(models.Model):
    categoryName = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=100, blank=True)
    # postingDate = models.DateField(default=date.today)

    def __str__(self):
        return f"{self.categoryName}"

class Sub_category(models.Model):
    subCategory = models.CharField(max_length=100)
    subCategoryDesc = models.CharField(max_length=100, blank=True)
    CategoryID = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.subCategory}"

# Posts here before

class Posts(models.Model):
    categoryID = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    subcategoryID = models.ForeignKey(Sub_category, on_delete=models.SET_NULL, null=True)
    postTitle = models.CharField(max_length=100, default='')
    postDetails = models.TextField()
    postingDate = models.DateField(default=date.today)
    postURL = models.URLField(blank=True, null=True)
    postImage = models.ImageField(upload_to='news_app/tmp/',blank=True, null=True)
    postedBy = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    lastUpdatedBy = models.CharField(max_length=50,default=date.today)
    volumeID = models.ForeignKey(News_volume_issue, on_delete=models.SET_NULL, null=True)
    isActive = models.BooleanField(default=True)
    slug=models.SlugField(null=True) #denote featured article

    def __str__(self):
        return f"Post Title: {self.postTitle}"

class Submission(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    category=models.CharField(max_length=50)
    postTitle = models.CharField(max_length=100, default='')
    postDetails = models.TextField()
    postingDate = models.DateField(default=date.today)
    postImage = models.ImageField(upload_to='news_app/tmp/',blank=True, null=True) #blank=True, null=True

    def __str__(self):
        return f" NAME: {self.name}, {self.category}"

