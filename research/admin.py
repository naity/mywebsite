from django.contrib import admin
from .models import Publication


# Register your models here.
class PublicationAdmin(admin.ModelAdmin):
    # show the title, pub_date, and number of downloads for each publication
    list_display = ("title", "pub_date", "downloads")

    # allow search gene by title
    search_fields = ["tittle"]

    # allow filter by pub_date
    list_filter = ['pub_date']

    # show at most 10 publications per page
    list_per_page = 10

admin.site.register(Publication, PublicationAdmin)
