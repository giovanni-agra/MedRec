from django.views import generic

from .forms import CreateAccount
from .models import GeneralPractitioner


# Create your views here.
class CreatePractitionerView(generic.CreateView):
    model = GeneralPractitioner
    template_name = 'MedRec/practitioner_form.html'
    form_class = CreateAccount
