from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views

urlpatterns = [
    path("create-website", views.create_website, name="create_website"),
    path("", views.website_data_list, name="website_data_list"),
    path("update-website/<str:id>", views.update_website_data, name="update_website_data"),
    path("delete-website-data/<str:pk>", views.delete_website_data, name="delete_website_data"),

]


