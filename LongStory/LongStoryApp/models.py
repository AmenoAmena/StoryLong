from django.db import models

# Create your models here.
class story(models.Model):
    story_shown = models.TextField(default=False)
    class Meta:
        verbose_name_plural = "story"