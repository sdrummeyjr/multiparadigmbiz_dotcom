from django.shortcuts import render
from django.db.models import Q
from .models import Topic, Entry
# from mpb_blog.apps import MpbBlogConfig
from django.apps import apps


def index(request):
    return render(request, 'index.html')


# https://stackoverflow.com/questions/46695150/django-search-fields-in-multiple-models
def search(request):
    query = request.GET.get('q')
    results = Entry.objects.filter(Q(title__contains=query) | Q(text__contains=query))
    context = {'query': query, 'results': results}
    return render(request, 'search.html', context)


def topics(request):
    """Show all topics"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'topics.html', context)


def topic(request, topic_id):
    """Show a single topic and all its entries"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'topic.html', context)


def entries(request):
    """Show all entries"""
    entries = Entry.objects.order_by('date_added')
    context = {'entries': entries}
    return render(request, 'entries.html', context)


def entry(request, entry_id):
    """Show a single entry"""
    entry = Entry.objects.get(id=entry_id)
    e_topics = entry.topic.all()
    # e_topics = ' | '.join(e_topics)
    context = {'entry': entry, 'topics': e_topics}
    return render(request, 'entry.html', context)
