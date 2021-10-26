from django.db import models


class Category(models.Model):
    
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_freindly_name(self):
        return self.friendly_name

class Article(models.Model):
    category = models.ManyToManyField('Category')
    name = models.CharField(max_length=254)
    summary = models.CharField(max_length=500)
    description = models.TextField()
    script_title_1 = models.CharField(max_length=254)
    script_1 = models.URLField(max_length=2000)
    codepen_title_1 = models.CharField(max_length=254, null=True, blank=True)
    codepen_data_slug_hash_1 = models.CharField(max_length=254, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
