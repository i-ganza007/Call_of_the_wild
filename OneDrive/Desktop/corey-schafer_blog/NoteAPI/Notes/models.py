from django.db import models
from django.conf import settings
from django.utils.timezone import now

class Notes(models.Model):
    class Status(models.TextChoices):
        URG = 'Urge', 'Urge'
        EASE = 'Ease', 'Ease'
        DEADLINE = 'Deadline', 'Deadline'
        SIMPLE = 'Simple', 'Simple'

    idx = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=20, blank=True)
    description = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.EASE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='author_name', on_delete=models.CASCADE)

    


    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', 'author'], name='No_two_notes_with_the_message'),
        ]

    def __str__(self):
        return f'{self.name} by {self.author.username}'



class Collections(models.Model):
    idx = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    notes = models.ManyToManyField(Notes)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='owner', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} with {self.notes.count()}'
