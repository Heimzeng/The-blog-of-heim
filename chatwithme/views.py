from django.shortcuts import render
def index(request):
    return render(request, 'chatwithme/index.html')
# Create your views here.
