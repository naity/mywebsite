from django.contrib import admin
from .models import Article


# class ArticleImageInline(admin.TabularInline):
# 	model = ArticleImage
# 	extra = 5

class ArticleAdmin(admin.ModelAdmin):
    # show the title, likes, and upload time for each photo
    list_display = ("title", "pub_date_time")

    # allow search gene by title
    search_fields = ["tittle"]

    # allow filter by upload time
    list_filter = ['pub_date_time']

    # show at most 10 photots per page
    list_per_page = 10

    # add images when creat article
    #inlines = [ArticleImageInline]


admin.site.register(Article, ArticleAdmin)