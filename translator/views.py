from django.shortcuts import render
from .models import Dictionary  # import the model
# Create your views here.


def homePage(request):
    query = request.GET.get("q", "")
    if query and query != "":
        result = Dictionary.objects.filter(english__contains=query).all()[:3]
        for data in result:
            print(data.uzbek)
    else:
        result = None
    return render(request, 'home.html', {"q": query, "result": result})
