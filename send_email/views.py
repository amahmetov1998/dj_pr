from django.views.generic import CreateView
from .forms import ContactForm
from .models import Contact
from .tasks import send_spam_email


class ContactView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'send_email/contact.html'
    success_url = '/send'

    def form_valid(self, form):
        form.save()
        send_spam_email.delay(form.instance.email)
        return super().form_valid(form)
