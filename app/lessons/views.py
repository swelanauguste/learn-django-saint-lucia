from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Lesson


class LessonListView(ListView):
    model = Lesson


class LessonDetailView(DetailView):
    model = Lesson
