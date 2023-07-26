import uuid

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
    from_warmup_emails_sent = models.PositiveIntegerField(default=0)

    # def __str__(self):
    #     return self.from_email
