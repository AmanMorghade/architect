from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def home_page(request):
    return render(request,'home.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            message = form.save()

            # Send email
            send_mail(
                f"New Contact Message: {message.name}",
                f"""
                Name: {message.name}
                Phone: {message.phone_number}
                Email: {message.email}
                Message: {message.question}
                """,
                settings.DEFAULT_FROM_EMAIL,
                [settings.CONTACT_EMAIL],
            )
            return redirect('contact')  # Or a thank you page
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})