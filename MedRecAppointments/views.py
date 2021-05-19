from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, CreateView, TemplateView, DetailView, UpdateView

from .forms import *


# Create your views here.

class PatientCreateView(PermissionRequiredMixin, CreateView):
    login_url = '/accounts/login/'
    model = PatientCreation
    template_name = 'MedRecAppointments/patient_form.html'
    form_class = CreatePatient
    success_url = '/'
    context_object_name = 'patient'
    permission_required = 'MedRecAppointments.add_patientcreation'

    def get_queryset(self):
        return PatientCreation.objects.all()


class AppointmentCreation(PermissionRequiredMixin, CreateView):
    login_url = '/accounts/login/'
    model = Appointment
    template_name = 'MedRecAppointments/appointment.html'
    form_class = AppointmentForm
    success_url = '/'
    permission_required = 'MedRecAppointments.add_appointment'


class AppointmentUpdateView(PermissionRequiredMixin, UpdateView):
    login_url = '/accounts/login/'
    model = Appointment
    template_name = 'MedRecAppointments/appointment.html'
    fields = ['status']
    success_url = '/'
    permission_required = 'MedRecAppointments.change_appointment'


class PrescriptionCreation(PermissionRequiredMixin, CreateView):
    login_url = '/accounts/login/'
    model = Prescription
    template_name = 'MedRecAppointments/prescription.html'
    form_class = PrescriptionForm
    success_url = '/'
    permission_required = 'MedRecAppointments.add_prescription'


class PrescriptionUpdateView(PermissionRequiredMixin, UpdateView):
    login_url = '/accounts/login/'
    model = Prescription
    fields = ['prescription']
    template_name = 'MedRecAppointments/prescription.html'
    success_url = '/'
    permission_required = 'MedRecAppointments.change_prescription'


class IndexView(PermissionRequiredMixin, ListView):
    login_url = '/accounts/login/'
    template_name = 'MedRecAppointments/index.html'
    context_object_name = 'appointment'
    permission_required = 'MedRecAppointments.view_prescription'

    def get_queryset(self):
        return Appointment.objects.all()

    def get_context_data(self, **kwargs):
        patient = super(IndexView, self).get_context_data(**kwargs)
        patient['patient'] = PatientCreation.objects.all()
        return patient


class MedHistoryAndPrescriptionList(LoginRequiredMixin, TemplateView):
    login_url = '/accounts/login/'
    template_name = 'MedRecAppointments/history&prescriptions.html'

    def get_context_data(self, **kwargs):
        context = super(MedHistoryAndPrescriptionList, self).get_context_data(**kwargs)
        context['prescription'] = Prescription.objects.all()
        context['patient'] = PatientCreation.objects.all()
        return context


class PrescriptionDetailView(PermissionRequiredMixin, DetailView):
    login_url = '/accounts/login/'
    model = Prescription
    template_name = 'MedRecAppointments/patientdetails.html'
    permission_required = 'MedRecAppointments.view_prescription'


class AccountantIndexView(PermissionRequiredMixin, ListView):
    login_url = '/accounts/login/'
    template_name = 'MedRecAppointments/accountant_index.html'
    context_object_name = 'invoice'
    permission_required = 'MedRecAppointments.view_payment'

    def get_queryset(self):
        return Payment.objects.all()


class InvoiceCreateView(PermissionRequiredMixin, CreateView):
    login_url = '/accounts/login/'
    model = Payment
    template_name = 'MedRecAppointments/payment_form.html'
    form_class = InvoiceForm
    success_url = '/accountant'
    permission_required = 'MedRecAppointments.add_payment'


class InvoiceView(PermissionRequiredMixin, DetailView):
    login_url = '/accounts/login/'
    model = Payment
    template_name = 'MedRecAppointments/invoice.html'
    permission_required = 'MedRecAppointments.view_payment'


class UpdateInvoiceView(LoginRequiredMixin, UpdateView):
    login_url = '/accounts/login/'
    model = Payment
    fields = ['paid']
    success_url = '/accountant'
    permission_required = 'MedRecAppointments.change_payment'
