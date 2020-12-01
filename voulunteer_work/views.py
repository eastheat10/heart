from django.shortcuts import render, get_object_or_404

# Create your views here.
def v_area(request):
    return render(request, 'v_area.html')

def v_detail(request):
    return render(request, 'v_detail.html')