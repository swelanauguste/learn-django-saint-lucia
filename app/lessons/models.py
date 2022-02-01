from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django_resized import ResizedImageField
from hitcount.models import HitCountMixin


class PublishedLessonManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status="published")


class Lesson(HitCountMixin, models.Model):
    LESSON_STATUSES = [
        ("draft", "Draft"),
        ("published", "Published"),
    ]
    status = models.CharField(max_length=25, choices=LESSON_STATUSES, default="draft")
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    description = models.TextField(blank=True)
    instructions = models.TextField(blank=True)
    image = ResizedImageField(
        size=[500, 300],
        upload_to="lesson_images",
        blank=True,
        null=True,
        default="img/lesson_default.png",
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    published_objects = PublishedLessonManager()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Lesson, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("lessons:lesson-detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title
