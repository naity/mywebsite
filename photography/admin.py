from django.contrib import admin
from .models import Photo
from .extract_exif import extract


class PhotoAdmin(admin.ModelAdmin):
    # show the title, likes, and upload time for each photo
    list_display = ("title", "likes", "taken_time")

    # allow search gene by title
    search_fields = ["tittle"]

    # allow filter by upload time
    list_filter = ['taken_time']

    # show at most 10 photots per page
    list_per_page = 10

    # Automatically save the exif information of photos
    def save_model(self, request, obj, form, change):
        obj.save()
        exif = extract(obj.image.path)
        # if exif informatino is available
        obj.camera = exif.get("camera")
        obj.lens = exif.get("lens")
        obj.focal_length = exif.get("focal_length")
        obj.f_stop = exif.get("f_stop")
        obj.shutter = exif.get("shutter")
        obj.iso = exif.get("iso")
        obj.taken_time = exif.get("taken_time")
        obj.save()


admin.site.register(Photo, PhotoAdmin)
