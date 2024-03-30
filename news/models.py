from django.db import models

class CategoryModel(models.Model):
    category_title = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_title

    class Meta:
        verbose_name = 'News category'
        verbose_name_plural = 'News categories'

class News(models.Model):
    title = models.CharField(max_length=50)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    country = models.CharField(max_length=30)
    date = models.DateField()
    description = models.TextField()
    image = models.FileField(upload_to='news_images')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


