from django.shortcuts import render
from .models import PageVisit

def home(request):
    page_title = "Inventory"
    PageVisit.objects.create(path = request.path)
    queryset = PageVisit.objects.all()
    
    return render(request, "core/home.html", {"page_title": page_title,
                  "queryset":queryset                            })
# Create your views here.
