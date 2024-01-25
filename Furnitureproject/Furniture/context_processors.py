from .models import Furniture


def menu_links(request):
    links = Furniture.objects.all()
    return dict(links=links)
