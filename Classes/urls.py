from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views

urlpatterns = [
    path("create-class-data",views.create_class_data,name="create_class_data"),
    path("class-data-list",views.class_data_list,name="class_data_list"),
    path("update-class-data/<str:id>",views.update_class_data,name="update_class_data"),
    path("delete-class-data/<str:pk>",views.delete_class_data,name="delete_class_data"),


]