from django.db import models
from django.utils.text import slugify


class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=True, blank=True)
    
    
    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.id}-{self.title}")
        super().save(*args, **kwargs)
        
        if  f'{str(self.id)}-' not in self.slug:
            self.slug = slugify(f"{self.id}-{self.title}")
            super().save(*args, **kwargs)
            
    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"
        ordering = [ "published_date"]
    