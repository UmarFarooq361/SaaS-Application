from django.shortcuts import render
from django.http import HttpResponse
from visits.models import PageVisits
def base(request):
    return render(request, 'base.html')

def home(request):
    queryset = PageVisits.objects.all()
    my_title = "umar farooq"
    context = {
        "my_title" :  my_title,
        "queryset" : queryset.count()
    }
    PageVisits.objects.create()
    return render(request, 'home.html', context)





