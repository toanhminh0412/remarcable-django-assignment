from django.views.generic import TemplateView
from .models import Category, Tag, Product

class IndexView(TemplateView):
    """
    Index page: /
    """
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = (
            Product.objects.all().prefetch_related('tag').select_related('category')
        )
        return context
