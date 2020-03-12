from django.shortcuts import render

# Create your views here.
from .forms import ContactForm


def contact_page(request):
    contact_form = ContactForm()
    context = {
        "title": "Help Center",
        "form": contact_form
    }
    return render(request, "ecommerce/contact_page.html", context)