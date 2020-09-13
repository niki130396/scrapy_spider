from django.db import models

# Create your models here.


class Parliment(models.Model):
    first_name = models.CharField(max_length=40, blank=True, null=True)
    middle_name = models.CharField(max_length=40, blank=True, null=True)
    last_name = models.CharField(max_length=40, blank=True, null=True)
    birth_date = models.CharField(max_length=30, blank=True, null=True)
    birth_place = models.CharField(max_length=50, blank=True, null=True)
    profession = models.CharField(max_length=50, blank=True, null=True)
    languages = models.CharField(max_length=100, blank=True, null=True)
    political_party = models.CharField(max_length=50, blank=True, null=True)
    email_address = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        app_label = 'parliment_api'
        db_table = 'parliment'
        managed = True
