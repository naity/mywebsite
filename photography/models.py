from django.db import models


# model for photos
class Photo(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    image = models.ImageField(upload_to='photography/photos')
    camera = models.CharField(max_length=300, blank=True, null=True)
    lens = models.CharField(max_length=300, blank=True, null=True)
    focal_length = models.CharField(max_length=300, blank=True, null=True)
    f_stop = models.CharField(max_length=300, blank=True, null=True)
    shutter = models.CharField(max_length=300, blank=True, null=True)
    iso = models.CharField(max_length=300, blank=True, null=True)
    likes = models.PositiveIntegerField(default=0)
    taken_time = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-taken_time',)
