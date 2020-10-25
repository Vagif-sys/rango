from django.views.generic import TemplateView

class Home(TemplateView):
    template_name = 'rango/home.html'


class About(TemplateView):
    template_name ="rango/about.html"