import uuid
from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


class EmailAccounts(models.Model):
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
    from_warmup_email_to_be_sent_time = models.DateTimeField(default=datetime.now())  # per day
