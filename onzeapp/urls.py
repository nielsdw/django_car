from django.urls import path
import onzeapp.views as views

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create_car, name="create_cars"),
    path("delete/", views.delete_car, name="delete")
]