from django.shortcuts import render
from django.http import HttpResponse


def tell_name(request):

    context = {"name": "Abhinav"}

    return render(request, "sample.html", context)
