# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class QuestionPage(models.Model):
    """
    Pagina de intrebari

    Ordonate dupa 'page_number'.
    """
    number = models.IntegerField(
        unique=True,
        help_text="Field pentru pastrat ordinea paginilor"
    )


class Question(models.Model):
    """
    Intrebare din survey de pe o anumita pagina.
    """
    page = models.ForeignKey(
        QuestionPage,
        on_delete=models.CASCADE,
        help_text="Pagina pe care apare aceasta intrebare"
    )
    text = models.TextField(
        help_text="Textul ce apare la inceputul intrebarii."
    )
    number = models.IntegerField(
        help_text="Pozitia pe pagina a intrebarii"
    )


class MultipleChoiceQuesition(Question):
    """
    Intrebare cu mai multe variante de raspuns
    """
    choice_1 = models.TextField(help_text="Valoarea 1")
    choice_2 = models.TextField(help_text="Valoarea 2")
    choice_3 = models.TextField(help_text="Valoarea 3")


class MultipleSelectQuestion(Question):
    """
    Intrebare cu un numar fix de optiuni. (Dropdown)
    """
    option_1 = models.TextField(help_text="Optiunea 1")
    option_2 = models.TextField(help_text="Optiunea 2")
    option_3 = models.TextField(help_text="Optiunea 3")


class FillInQuestion(Question):
    """
    Intrebare cu casuta text de completat.
    """
    answer = models.TextField(help_text="Raspunsul primit")
