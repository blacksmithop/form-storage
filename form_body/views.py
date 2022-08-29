from django.shortcuts import render
from django.http import JsonResponse

from .forms import PersonForm
from .models import Person


def tell_name(request):

    context = {"name": "Abhinav"}

    return render(request, "sample.html", context)


def save_name(request):

    if request.method == "POST":

        form = PersonForm(request.POST, request.FILES)

        if form.is_valid():

            payload = request.POST.dict()
            del payload["csrfmiddlewaretoken"]

            return JsonResponse(payload)

    else:
        form = PersonForm()

    return render(request, "form.html", {"form": form})
