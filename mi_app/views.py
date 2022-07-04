from django.shortcuts import render
from django.http import HttpResponse
from mi_app.models import Familiar

# Create your views here.


def listar(request):
    context = {

        "familiares": Familiar.objects.all()

    }

    return render(request, "mi_app/familiares.html", context)   