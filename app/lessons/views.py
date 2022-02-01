from django.shortcuts import render
from django.views.generic import ListView, DetailView
from hitcount.views import HitCountDetailView, HitCountMixin

from .models import Lesson


class LessonListView(HitCountMixin, ListView):
    model = Lesson
    count_hit = True

    def get_queryset(self):
        queryset = Lesson.published_objects.all()
        return queryset


class LessonDetailView(HitCountDetailView):
    model = Lesson
    count_hit = True
