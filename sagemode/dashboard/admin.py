from django.contrib import admin
from .models import EmailAccount, Campaign, CampaignEmail

# Register your models here.
admin.site.register(EmailAccount)
admin.site.register(Campaign)
admin.site.register(CampaignEmail)
