from urllib.parse import urlparse
from django.urls import path

from . import views

app_name = "lessons"


urlpatterns = [
    path("", views.LessonListView.as_view(), name="lesson-list"),
    path("<slug:slug>", views.LessonDetailView.as_view(), name="lesson-detail"),
]
