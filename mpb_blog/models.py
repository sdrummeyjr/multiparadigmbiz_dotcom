from django.db import models


class Topic(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class EntryType(models.Model):
    name = models.CharField(max_length=15)
    description = models.CharField(max_length=75, default='')

    def __str__(self):
        return f"{self.name}"


class Entry(models.Model):
    entry_type = models.ForeignKey(EntryType, default=1, on_delete=models.CASCADE)
    topic = models.ManyToManyField(Topic)
    title = models.CharField(max_length=100, blank=False, default='default')
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        topics = [f'{item.text}' for item in self.topic.all()[:3]]
        return f"{self.title} - {', '.join(topics)}"
