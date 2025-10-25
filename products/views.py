from django.views.generic import TemplateView

class IndexView(TemplateView):
    """
    Index page: /
    """
    template_name = "index.html"
