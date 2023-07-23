from allauth.account.decorators import verified_email_required
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


@login_required
def index(request):
    return HttpResponse("Hello, world.")
