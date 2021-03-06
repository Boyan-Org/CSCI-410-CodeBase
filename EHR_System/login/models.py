from django.db import models


# Create your models here.
class Account(models.Model):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    role = models.CharField(
        max_length=20,
        choices=(
            ('admin', 'admin'),
            ('medical_staff', 'medical staff'),
            ('patient', 'patient'),
        )
    )

    class Meta:
        db_table = 'account'
