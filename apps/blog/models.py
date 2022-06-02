from django.db import models


class Timestamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Tag(Timestamp):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Post(Timestamp):
    title = models.CharField(max_length=250)
    tags = models.ManyToManyField(Tag, blank=True)
    image = models.ImageField(upload_to='blog/', null=True)
    content = models.TextField()

    def __str__(self):
        return self.title

