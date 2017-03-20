from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.utils import timezone
from .models import Publication


class IndexView(generic.ListView):
    """
    Index page will display a list of the papers in the database.
    Includes a figure, the title, and abstract.
    """

    template_name = "research/index.html"
    context_object_name = "publications"

    def get_queryset(self):
        all_publications = Publication.objects.all()

        # use Django's Paginator to display 5 publications per page
        paginator = Paginator(all_publications, 5)

        # last page
        self.last_page = paginator.num_pages

        page = self.request.GET.get("page", 1)

        try:
            publications = paginator.page(page)
        except PageNotAnInteger:
            publications = paginator.page(1)
        except EmptyPage:
            publications = paginator.page(self.last_page)

        return publications

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        # add time filter and order_by info
        context["last_page"] = self.last_page

        return context


def count_downloads(request):
    """This view counts how many times each paper has been downloaded."""
    if request.method == "GET":
        publication_id = request.GET.get("publication_id")

        if publication_id:
            publication = Publication.objects.get(pk=int(publication_id))
            if publication:
                # update the count and date downloaded
                publication.downloads += 1
                publication.last_downloaded = timezone.now()
                publication.save()

    # just return okay
    return HttpResponse('okay')
