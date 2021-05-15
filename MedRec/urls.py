from django.urls import path
from . import views

app_name = 'MedRec'
urlpatterns = [
    path('createpractitioner/', views.CreatePractitionerView.as_view(), name='addPractitioner')
]