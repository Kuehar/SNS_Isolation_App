from django.views import generic

# Create your views here.

class TopView(generic.TemplateView):
    template_name = 'top/index.html'
