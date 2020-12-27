from django.urls import path
from .views import (
    user_info_form_view,
    user_code_form_view,
)

urlpatterns = [
    path("", user_info_form_view, name="informatii_utilizator"),
    path("cod_utilizator/", user_code_form_view, name="cod_utilizator"),
]
