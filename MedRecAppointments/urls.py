from django.urls import path

from . import views

app_name = 'MedRecAppointments'
urlpatterns = [
    path('', views.IndexView.as_view(), name='Index'),
    path('addpatient/', views.PatientCreateView.as_view(), name='addPatient'),
    path('appointmentcreation/', views.AppointmentCreation.as_view(), name='createAppointment'),
    path('createprescription/', views.PrescriptionCreation.as_view(), name='createPrescription'),
    path('medhistory&prescriptions/', views.MedHistoryAndPrescriptionList.as_view(), name='historyAndPrescriptions'),
    path('patientdetails/<int:pk>', views.PatientView.as_view(), name='patientDetails'),
]
