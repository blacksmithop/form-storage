from http import client
from django.shortcuts import render
from .forms import NameForm
from django.http import JsonResponse
from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017/")
db = client["file_upload"]

collection = db["test"]


def tell_name(request):

    context = {"name": "Abhinav"}

    return render(request, "sample.html", context)


def save_name(request):

    if request.method == "POST":

        form = NameForm(request.POST, request.FILES)
        print(request.FILES)

        if form.is_valid():

            data = {"name": request.POST.get("name")}

            collection.insert_one(data)

            return JsonResponse(data)

    else:
        form = NameForm()

    return render(request, "form.html", {"form": form})
