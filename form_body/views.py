from django.shortcuts import render
from .forms import NameForm
from django.http import JsonResponse


def tell_name(request):

    context = {"name": "Abhinav"}

    return render(request, "sample.html", context)


def save_name(request):

    if request.method == "POST":

        form = NameForm(request.POST, request.FILES)
        print(request.FILES)

        if form.is_valid():
            return JsonResponse({"name": request.POST.get("name")})

    else:
        form = NameForm()

    return render(request, "form.html", {"form": form})
