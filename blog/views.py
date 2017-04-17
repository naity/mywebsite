from django.shortcuts import render
from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Article

class IndexView(generic.ListView):
    """
    Index page will display a list of the articles in the database.
    """

    template_name = "blog/index.html"
    context_object_name = "articles"

    def get_queryset(self):
        article_list = Article.objects.order_by('-pub_date_time', '-pk')

        # use Django's Paginator to display 3 articles
        paginator = Paginator(article_list, 3)

        # last page
        self.last_page = paginator.num_pages

        page = self.request.GET.get("page", 1)

        try:
            articles = paginator.page(page)
        except PageNotAnInteger:
            articles = paginator.page(1)
        except EmptyPage:
            articles = paginator.page(self.last_page)

        return articles

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context["last_page"] = self.last_page

        return context