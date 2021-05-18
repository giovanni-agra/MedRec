from django.db import models

from MedRec.models import Account


# Create your models here.
class PatientCreation(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(choices=[
        ('F', 'Female'),
        ('M', 'Male'),
    ], max_length=20)
    age = models.IntegerField()
    passport_number = models.CharField(max_length=255, unique=True)
    email = models.EmailField(blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Appointment(models.Model):
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(choices=[
        ('Incomplete', 'Incomplete'),
        ('Complete', 'Complete')
    ], max_length=20)
    patient = models.ForeignKey(PatientCreation, on_delete=models.CASCADE)
    nurse = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='Nurse')
    doctor = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='Doctor')


class Prescription(models.Model):
    doctor = models.ForeignKey(Account, on_delete=models.CASCADE)
    patient = models.ForeignKey(PatientCreation, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    diagnosis = models.CharField(max_length=255, blank=True)
    symptoms = models.CharField(max_length=500)
    prescription = models.TextField()

    def __str__(self):
        return "Prescription Doc:{} Patient:{}".format(self.doctor.last_name, self.patient)


class Payment(models.Model):
    patient = models.ForeignKey(PatientCreation, on_delete=models.CASCADE, related_name='patient_payment')
    date = models.DateField(auto_now_add=True)
    cost = models.IntegerField(null=True)
    paid = models.IntegerField(null=True)
    debt = models.IntegerField(null=True)
    total_amount = models.IntegerField(null=True, default=0)

    def calculate_debt(self):
        debt = self.cost - self.paid
        return debt

    def calculate_total_amount(self):
        total_amount = self.total_amount + self.debt
        return total_amount

    def save(self, *args, **kwargs):
        self.debt = self.calculate_debt()
        self.total_amount = self.calculate_total_amount()
        super().save(*args, **kwargs)

    def __str__(self):
        return "Payment Patient:{} Amount:{}".format(self.patient, self.total_amount)
