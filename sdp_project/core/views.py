from django.views import generic, View

class Homeview(generic.TemplateView):
    template_name = "templates/home/index.html"