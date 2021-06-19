from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'short_url_site/index.html')