from django.shortcuts import render
from matchday360.models import Matchday
from django.core.paginator import Paginator
from feedback.models import Feedback


# Create your views here.
def homePage(request):
    return render(request, "detailviews/homepage.html")


def detailPage(request, title):
    id_start_index = title.rfind("-") + 1
    ids = title[id_start_index:]
    matchday = Matchday.objects.get(id=ids)
    context = {"matchday": matchday}
    return render(request, "detailviews/detailpage.html", context=context)


def listView(request):
    matches = Matchday.objects.all()
    paginator = Paginator(matches, 4)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
    }
    return render(request, "indexviews/listview.html", context=context)


def contactus(request):
    name = request.POST.get("name")
    email = request.POST.get("email")
    message = request.POST.get("message")
    if name and email and message:
        Feedback.objects.create(name=name, email=email, message=message)
        alert_success = True
    else:
        alert_success = False
    context = {"alert_success": alert_success}
    return render(request, "detailviews/contactus.html", context=context)
