from django.db import models
import uuid

# Create your models here.

class Tag(models.Model):
    tag1 = models.SlugField(
        max_length=20,
        blank=True,
        null=True
    )
    tag2 = models.SlugField(
        max_length=20,
        blank=True,
        null=True
    )
    tag3 = models.SlugField(
        max_length=20,
        blank=True,
        null=True
    )
    def __str__(self):
        return self.tag1

class Note(models.Model):
    name = models.CharField(max_length=255)
    # tag1 = models.SlugField(
    # 	max_length=20,
    # 	blank=True,
    # 	null=True
    # )
    # tag2 = models.SlugField(
    # 	max_length=20,
    # 	blank=True,
    # 	null=True
    # )
    # tag3 = models.SlugField(
    # 	max_length=20,
    # 	blank=True,
    # 	null=True
    # )
    # tag = models.ForeignKey(Tags)
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True)
    unique_identity = models.UUIDField(primary_key=True, default=uuid.uuid4())
    note = models.TextField(blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name
