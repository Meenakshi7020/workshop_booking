from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings

# Local Imports
from cms.models import Page


def index(request):
    page = Page.objects.filter(title=settings.HOME_PAGE_TITLE)
    if page.exists():
        redirect_url = reverse("cms:home", args=[page.first().permalink])
    else:
        redirect_url = reverse("workshop_app:index")
    return redirect(redirect_url)


# ✅ New View for Statistics
def statistics(request):
    return render(request, 'workshop_app/statistics.html')
