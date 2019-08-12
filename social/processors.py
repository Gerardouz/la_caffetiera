from .models import Enlace
def ext_context(request):
    ctx = {}
    social = Enlace.objects.all()
    for link in social:
        ctx[link.key] = link.url
    return ctx
