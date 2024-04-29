from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class Home(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        self.request.session["my_name"]="arsalan"
        del self.request.session["my_name"]
        # print(self.request.session["my_name"])
        # print(self.request.session.get("my_name","bardia"))#برای اینکه اگر my_name نبود خطا نده
        return context