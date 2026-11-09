from django.contrib import admin
from django.urls import path
from portfolio import views

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", views.home, name="home"),
    path("contact/", views.contact, name="contact"),

    path("projects/<slug:slug>/", views.project_detail, name="project_detail"),
    path("services/<slug:slug>/", views.service_detail, name="service_detail"),

    path("admin-login/", views.admin_login, name="admin_login"),
    path("admin-logout/", views.admin_logout, name="admin_logout"),
    path("dashboard/", views.dashboard, name="dashboard"),

    # Live message notification API
    path("dashboard/new-messages/", views.new_messages, name="new_messages"),
]