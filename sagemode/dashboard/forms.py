from django.forms import ModelForm
from .models import EmailAccounts


class AddEmailsForm(ModelForm):
    class Meta:
        model = EmailAccounts
        fields = [
            "from_email", "from_password", "from_imap_address", "from_imap_port", "from_smtp_address", "from_smtp_port"
        ]
