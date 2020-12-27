# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import UserDataForm, UserCodeForm

# Create your views here.
def user_info_form_view(request):
    if request.method == "POST":
        form = UserDataForm(request.POST)
        if form.is_valid():
            varsta = form.cleaned_data.get("varsta")
            gen = form.cleaned_data.get("gen")
            tip_personal = form.cleaned_data.get("tip_personal")
            grad_militar = form.cleaned_data.get("grad_militar")
            durata_functie_ani = form.cleaned_data.get("durata_functie_ani")
            durata_functie_luni = form.cleaned_data.get("durata_functie_luni")
            durata_unitate_ani = form.cleaned_data.get("durata_unitate_ani")
            durata_unitate_luni = form.cleaned_data.get("durata_unitate_luni")
            ore_pe_zi = form.cleaned_data.get("ore_pe_zi")
            ture = form.cleaned_data.get("ture")
            program_ture = form.cleaned_data.get("program_ture")

            experienta_functie = (
                str(durata_functie_ani) + " ani " + str(durata_functie_luni) + " luni "
            )
            experienta_unitate = (
                str(durata_unitate_ani) + " ani " + str(durata_unitate_luni) + " luni "
            )

            data = {
                "form": form,
                "varsta": varsta,
                "gen": gen,
                "tip_personal": tip_personal,
                "grad_millitar": grad_militar,
                "experienta_functie": experienta_functie,
                "experienta_unitate": experienta_unitate,
                "ore_pe_zi": ore_pe_zi,
                "ture": ture,
                "program_ture": program_ture,
            }

            # TO DO : redirect data where we will use it.
            return render(request, "informatii_utilizator.html", data)

    else:
        form = UserDataForm()

    return render(request, "informatii_utilizator.html", {"form": form})


def user_code_form_view(request):
    if request.method == "POST":
        form = UserCodeForm(request.POST)
        if form.is_valid():
            print("form is valid")
            litera_oras = form.cleaned_data.get("litera_oras")
            litera_judet = form.cleaned_data.get("litera_judet")
            suma_cifre_an_nastere = form.cleaned_data.get("suma_cifre_an_nastere")
            suma_cifre_zi_luna = form.cleaned_data.get("suma_cifre_zi_luna")

            cod_utilizator = (
                litera_oras
                + litera_judet
                + str(suma_cifre_an_nastere)
                + str(suma_cifre_zi_luna)
            )

            # TO DO : redierect this where it needs to be.
            return render(
                request, "cod_utilizator.html", {"form": form, "cod": cod_utilizator}
            )

    else:
        form = UserCodeForm()

    return render(request, "cod_utilizator.html", {"form": form})
