from django.forms import ModelForm

from .models import *


class CreatePatient(ModelForm):
    class Meta:
        model = PatientCreation
        fields = ['first_name', 'last_name', 'gender', 'age', 'passport_number', 'email']


class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AppointmentForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['patient'].queryset = PatientCreation.objects.all()
            self.fields['doctor'].queryset = Account.objects.filter(position='Practitioner')
            self.fields['nurse'].querysest = Account.objects.filter(position='Nurse')


class PrescriptionForm(ModelForm):
    class Meta:
        model = Prescription
        fields = ('patient', 'doctor', 'diagnosis', 'symptoms', 'prescription')

    def __init__(self, *args, **kwargs):
        super(PrescriptionForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['patient'].queryset = PatientCreation.objects.all()
            self.fields['doctor'].queryset = Account.objects.filter(position='Practitioner')


class InvoiceForm(ModelForm):
    class Meta:
        model = Payment
        fields = ('patient', 'cost', 'paid')

        def __init__(self, *args, **kwargs):
            super(InvoiceForm, self).__init__(*args, **kwargs)
            if self.instance:
                self.fields['patient'].queryset = Prescription.objects.all()
