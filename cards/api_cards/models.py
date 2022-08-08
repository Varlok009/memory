from django.db import models


class MemoryCard(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField(blank=True)
    date_create = models.DateTimeField(auto_now_add=True)
    date_last_show = models.DateTimeField()
    date_remind = models.DateTimeField()

    def __str__(self):
        return self.question
