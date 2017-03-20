from django.db import models


# model for publications
class Publication(models.Model):
    title = models.CharField(max_length=300)
    authors = models.TextField()
    abstract = models.TextField()
    figure = models.ImageField(upload_to='research/publications/figures')
    pdf = models.FileField(upload_to='research/publications/pdfs')
    pub_date = models.DateField()
    downloads = models.PositiveIntegerField(default=0)
    # must set both null and blank to True, null is used for database,
    # while blank is used for forms
    last_downloaded = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-pub_date',)
