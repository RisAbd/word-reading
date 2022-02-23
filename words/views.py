from django.shortcuts import render

# Create your views here.

from . import models


def index(request):

    words = models.Word.objects.filter(enabled=True).order_by('?').all()

    return render(request, 'words/index.html', dict(words=words))
