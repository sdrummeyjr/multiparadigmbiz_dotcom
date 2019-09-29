from django.urls import path
from . import views

app_name = 'mpb_blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    path('entries/', views.entries, name='entries'),
    path('entries/<int:entry_id>/', views.entry, name='entry'),
]
