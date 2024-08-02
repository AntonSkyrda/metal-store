from django.shortcuts import render, redirect

from .models import PhoneNumber
from .forms import ContactForm


def index(request):
    phone_numbers = PhoneNumber.objects.all()
    
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("contacts:index")
    else:
        form = ContactForm()

    context = {
        "phone_numbers": phone_numbers,
        "form": form
    }
    
    return render(request, "contacts/index.html", context)
    