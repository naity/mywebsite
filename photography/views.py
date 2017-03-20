import json
from django.views import generic
from django.http import HttpResponse
from .models import Photo


class IndexView(generic.ListView):
    """
    Index page will display my portfolio of photos.
    Includes gene name, alias, and summary.
    """

    template_name = "photography/index.html"
    model = Photo
    context_object_name = "photos"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context["liked"] = self.request.session.get("liked")

        if context["liked"]:
            # convert string to dictionary
            context["liked"] = json.loads(context["liked"])

        return context


def like_photo(request):
    """This view counts the number of likes a photo get"""
    if request.method == "GET":
        photo_id = request.GET.get("photo_id")

        if photo_id:
            photo = Photo.objects.get(pk=int(photo_id))
            if photo:
                # update the number of likes
                photo.likes += 1
                photo.save()

                # write the liked cookie
                if request.session.get("liked"):
                    # convert string to dictionary
                    liked = json.loads(request.session['liked'])
                else:
                    liked = {}

                # record that the user has liked the photo
                liked[photo_id] = "true"
                # convert dictionary back to string
                # note that photo_id will also be converted to str
                liked = json.dumps(liked)

                request.session["liked"] = liked

    return HttpResponse(photo.likes)
