from django import template

register = template.Library()


@register.assignment_tag
def get_author_list(publication):
    return publication.authors.split(",")


@register.filter
def is_me(author):
    return author == "Yuan Tian"


@register.filter
def is_last(author, author_list):
    return author == author_list[-1]
