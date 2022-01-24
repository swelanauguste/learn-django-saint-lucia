from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Lesson


class LessonListView(ListView):
    model = Lesson
    
    def get_queryset(self):
        queryset = Lesson.published_objects.all()
        return queryset
    


class LessonDetailView(DetailView):
    model = Lesson
