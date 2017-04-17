from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Article(models.Model):
    """Model for blog articles."""
    title = models.CharField(max_length=300)
    abstract = RichTextUploadingField()
    text = RichTextUploadingField()
    pub_date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Use question as representation of Answer object."""
        return self.title
    
    class Meta:
        ordering = ('-pub_date_time',)

# class ArticleImage(models.Model):
# 	# one article may have many images
#     article = models.ForeignKey(Article)
#     title = models.CharField(max_length=300)
#     image = models.ImageField(upload_to='blog/pictures')
#     upload_date_time = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.title

#     class Meta:
#         ordering = ('-upload_date_time',)