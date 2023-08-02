from allauth.account.decorators import verified_email_required
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.generic import DeleteView

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


@login_required()
def show_email_details_view(request, pk):
    query_results = EmailAccounts.objects.filter(sagemode_user=request.user, pk=pk).values()
    form = None

    for email_value in query_results:
        form = AddEmailsForm(initial={
            "from_email": email_value["from_email"],
            "from_password": email_value["from_password"],
            "from_imap_address": email_value["from_imap_address"],
            "from_imap_port": email_value["from_imap_port"],
            "from_smtp_address": email_value["from_smtp_address"],
            "from_smtp_port": email_value["from_smtp_port"],
        })
        break

    return render(request, "dashboard/show_email_details.html", {"form": form, "email_details": query_results})


# @login_required()
# def delete_email_view(request, pk):
#     # email_to_be_deleted = get_object_or_404(EmailAccounts, pk=pk)
#     # url = reverse('emails')
#     # return HttpResponseRedirect(url)
#     # if request.method == "POST":
#     #     email_to_be_deleted.delete()
#     #     print(f"{pk} deleted")
#     #     url = reverse('emails')
#     #     return HttpResponseRedirect(url)
#     return HttpResponseRedirect(reverse("delete_email_view"))
#     # return render(request, "dashboard/emails.html")


@method_decorator(login_required, name="dispatch")
class DeleteEmailView(DeleteView):
    model = EmailAccounts
    context_object_name = 'email'
    success_url = reverse_lazy('dashboard:emails')

    def form_valid(self, form):
        messages.success(self.request, "The email account was deleted successfully.")
        return super(DeleteEmailView, self).form_valid(form)


def dummy_view(request):
    return render(request, "dashboard/dummy.html")


@login_required()
def campaigns_view(request):
    return render(request, "dashboard/campaigns.html")


@login_required()
def settings_view(request):
    return render(request, "dashboard/settings.html")
