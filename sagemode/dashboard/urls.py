from django.urls import path

from . import views

app_name = 'dashboard'
# urlpatterns = [
#     path("", views.IndexView.as_view(), name="index"),
#     path("emails/", views.EmailsView.as_view(), name="emails"),
# ]

urlpatterns = [
    path("", views.EmailsView.as_view(), name="emails"),
    path("emails/", views.EmailsView.as_view(), name="emails"),
    path("emails/add/", views.add_emails, name="add_emails"),
    path("emails/<uuid:pk>/", views.show_email_details_view, name="show_email_details"),
    # path("emails/delete/<uuid:pk>/", views.delete_email_view, name="delete_email_view"),
    path("emails/delete/<uuid:pk>/", views.DeleteEmailView.as_view(), name="delete_email_view"),
    path("dummy/", views.dummy_view, name="dummy_view"),
    path("campaigns/", views.campaigns_view, name="campaigns_view"),
    path("settings/", views.settings_view, name="settings_view"),
]
