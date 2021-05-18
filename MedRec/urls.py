from django.urls import path

from . import views

app_name = 'MedRec'
urlpatterns = [
    path('addAccount/', views.AccountCreation.as_view(), name='addAccount'),
    path('', views.AllAccountsList.as_view(), name='index'),
]
