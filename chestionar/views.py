# -*- coding: utf-8 -*-
from django.views.generic import TemplateView
from survey.models import Response

from survey.views import ConfirmView, IndexView, SurveyCompleted
from survey import views as survery_views

import logging
from datetime import date

from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.shortcuts import redirect, render, reverse
from django.views.generic import View

from survey.models import Survey
from survey.decorators import survey_available
from survey.forms import ResponseForm


LOGGER = logging.getLogger(__name__)

class IndexView(survery_views.IndexView):
    template_name = "starting_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["survey"] = context["surveys"][0]
        return context


class SurveyDetail(survey_views.Detail):

    @survey_available
    def get(self, request, *args, **kwargs):
        survey = kwargs.get("survey")
        step = kwargs.get("step", 0)
        template_name = "question_page.html"

        form = ResponseForm(survey=survey, user=request.user, step=step)
        categories = form.current_categories()

        asset_context = {
            # If any of the widgets of the current form has a "date" class, flatpickr will be loaded into the template
            "flatpickr": any([field.widget.attrs.get("class") == "date" for _, field in form.fields.items()])
        }
        context = {
            "response_form": form,
            "survey": survey,
            "categories": categories,
            "step": step,
            "asset_context": asset_context,
        }

        return render(request, template_name, context)

    @staticmethod
    def handle_invalid_form(context, form, request, survey):
        LOGGER.info("Non valid form: <%s>", form)
        return render(request, "question_page.html", context)
