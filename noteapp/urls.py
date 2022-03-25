from django.urls import path
from noteapp.views import NoteList, NoteDetail, TagList, TagDetail

urlpatterns = [
    path('notes/', NoteList.as_view(), name='note-list'),
    path('notes/<int:pk>', NoteDetail.as_view(), name='note-detail'),
    path('tags/', TagList.as_view(), name='tag-list'),
    path('tags/<int:pk>', TagDetail.as_view(), name='tag-detail'),
  
]