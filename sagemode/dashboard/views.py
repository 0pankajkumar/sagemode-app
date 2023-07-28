from allauth.account.decorators import verified_email_required
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import generic

from .forms import AddEmailsForm
from .models import EmailAccounts


# @login_required()
# class IndexView:
#     template_name = "dashboard/emails.html"
#
#
# class EmailsView:
#     template_name = "dashboard/emails.html"


@login_required
def index(request):
    return HttpResponse("Home of dashboard")


# @login_required
# def emails(request):
#     return HttpResponse("All emails here with list")

@method_decorator(login_required, name="dispatch")
class EmailsView(generic.ListView):
    template_name = "dashboard/emails.html"
    context_object_name = "all_emails_list"

    def get_queryset(self):
        # print(self.request)
        # for attr, value in self.request.__dict__.items():
        #     print(attr, value)
        return EmailAccounts.objects.filter(sagemode_user=self.request.user)


@login_required
def add_emails(request):
    if request.method == "POST":
        form = AddEmailsForm(request.POST)
        if form.is_valid():
            new_email = form.save(commit=False)
            new_email.sagemode_user = request.user
            new_email.save()
            return redirect("dashboard:emails")
        else:
            raise ValidationError("Form data is invalid")

    else:
        form = AddEmailsForm()
        return render(request, "dashboard/add_emails.html", {"form": form})


def dummy_view(request):
    return render(request, "dashboard/dummy.html")
