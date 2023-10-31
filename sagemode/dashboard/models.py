import time
import uuid
from datetime import datetime

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class EmailAccount(models.Model):
    from_email_account_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sagemode_user = models.ForeignKey(User, on_delete=models.CASCADE)
    from_email_account_id_status = models.CharField(
        max_length=10,
        choices=[('ACTIVE', 'ACTIVE'), ('INACTIVE', 'INACTIVE'), ('DELETED', 'DELETED')],
        default='INACTIVE',
    )
    from_email = models.EmailField(unique=True)
    from_password = models.CharField(max_length=100)
    from_imap_address = models.CharField(max_length=200)
    from_imap_port = models.PositiveIntegerField()
    from_smtp_address = models.CharField(max_length=200)
    from_smtp_port = models.PositiveIntegerField()
    from_warmup_emails_sent_per_week = models.PositiveIntegerField(default=0)  # per week
    from_warmup_emails_to_be_sent_today = models.PositiveIntegerField(default=0)  # per day
    from_warmup_email_to_be_sent_time = models.DateTimeField(default=timezone.now)  # per day


def current_time():
    return timezone.now().time()


class Campaign(models.Model):
    sagemode_user = models.ForeignKey(User, on_delete=models.CASCADE)
    campaign_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    campaign_name = models.CharField(max_length=100)
    campaign_active = models.BooleanField(default=True)
    sending_time = models.TimeField(default=current_time)
    composed_text = models.CharField(max_length=2000)


class CampaignEmail(models.Model):
    campaign_name = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    email_id = models.EmailField(unique=True)
    email_active = models.BooleanField(default=True)

