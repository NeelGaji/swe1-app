from django.shortcuts import render


def index(request):
    # render a simple page with a single-select question
    return render(request, 'polls/index.html')