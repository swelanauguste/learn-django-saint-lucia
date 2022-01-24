from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django_resized import ResizedImageField


class Lesson(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    description = models.TextField(blank=True)
    image = ResizedImageField(size=[500, 300], upload_to='lesson_images', blank=True, null=True, default='img/lesson_default.png')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title + "-" + str(self.updated_at))
        super(Lesson, self).save(*args, **kwargs)
        
    def get_absolute_url(self):
        return reverse("lessons:lesson-detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title
