from django.db import models
from django.utils.text import slugify
from django.db.models.signals import post_save
from django.dispatch import receiver


class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True)
    

    
    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         super().save(*args, **kwargs)  # İlk dəfə `save()`, ID təyin olunsun
    #         self.slug = slugify(f'{self.title}-{self.id}')
    #         return super().save(*args, **kwargs)  # Yenidən save et
    #     super().save(*args, **kwargs)
            
    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"
        ordering = [ "published_date"]
   
# slug with id 
        
@receiver(post_save, sender=Book)
def create_book_slug(sender, instance, created, **kwargs):
    if created and not instance.slug:
        instance.slug = slugify(f'{instance.id}-{instance.title}')
        instance.save()


# without id

# def unique_slugify(instance, title):
#     slug = slugify(title)
#     Klass = instance.__class__
#     num = 1
#     while Klass.objects.filter(slug=slug).exists():
#         slug = f"{slug}-{num}"
#         num += 1
#     return slug

# @receiver(post_save, sender=Book)
# def create_book_slug(sender, instance, created, **kwargs):
#     if created and not instance.slug:
#         instance.slug = unique_slugify(instance, instance.title)
#         instance.save(update_fields=['slug'])