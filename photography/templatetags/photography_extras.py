from django import template

register = template.Library()


@register.filter
def is_not_liked(photo_id, liked):
    photo_id = str(photo_id)
    # check if a photo has been liked by the current user
    if liked:
        if liked.get(photo_id) == "true":
            return False
        else:
            return True
    return True
