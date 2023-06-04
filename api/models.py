from django.db import models


# Create your models here.


class Users(models.Model):
    username = models.CharField(max_length=255, help_text=("USERNAME"))
    useremail = models.EmailField(max_length=255, help_text=("EMAIL_ADDRESS"))
    credit_card_number = models.IntegerField(help_text=("CREDIT_CARD_NUMBER"))
    created_timestamp = models.DateField(help_text=("N/A"))
