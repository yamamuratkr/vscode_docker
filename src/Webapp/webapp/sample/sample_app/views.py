from django.shortcuts import render
from django.http import HttpResponse
from sample_app.models import SampleText

# Create your views here.
def index(request):
    index_text = SampleText.objects.get().sample_text
    return HttpResponse(index_text)