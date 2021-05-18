from django.urls import path

from . import views

app_name = 'MedRecAppointments'
urlpatterns = [
    path('', views.IndexView.as_view(), name='Index'),
    path('addpatient/', views.PatientCreateView.as_view(), name='addPatient'),
    path('appointmentcreation/', views.AppointmentCreation.as_view(), name='createAppointment'),
    path('appointmentupdate/<int:pk>', views.AppointmentUpdateView.as_view(), name='updateAppointment'),
    path('createprescription/', views.PrescriptionCreation.as_view(), name='createPrescription'),
    path('medhistory&prescriptions/', views.MedHistoryAndPrescriptionList.as_view(), name='historyAndPrescriptions'),
    path('patientdetails/<int:pk>', views.PrescriptionDetailView.as_view(), name='patientDetails'),
    path('accountant/', views.AccountantIndexView.as_view(), name='AccountantIndex'),
    path('accountant/createinvoice/', views.InvoiceCreateView.as_view(), name='createInvoice'),
    path('accountant/invoicedetails/<int:pk>', views.InvoiceView.as_view(), name='invoiceDetails'),
    path('accountant/updateinvoice/<int:pk>', views.UpdateInvoiceView.as_view(), name='invoiceUpdate'),
    path('updateprescription<int:pk>/', views.PrescriptionUpdateView.as_view(), name='updatePrescription'),
]
