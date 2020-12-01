from django.shortcuts import render
from django.views.generic. base import TemplateView

# Create your views here.
def MainpageView(request):
    # template_name = 'theme/main.html'
    return render(request,'index.html')