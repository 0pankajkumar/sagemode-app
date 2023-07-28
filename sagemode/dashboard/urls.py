from django.urls import path

from . import views

app_name = 'dashboard'
# urlpatterns = [
#     path("", views.IndexView.as_view(), name="index"),
#     path("emails/", views.EmailsView.as_view(), name="emails"),
# ]

urlpatterns = [
    path("", views.index, name="index"),
    path("emails/", views.EmailsView.as_view(), name="emails"),
    path("emails/add/", views.add_emails, name="add_emails"),
    path("dummy/", views.dummy_view, name="dummy_view"),
]
