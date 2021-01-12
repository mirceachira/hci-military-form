# -*- coding: utf-8 -*-
import logging

from django.shortcuts import render
from survey import views as survey_views
from survey.models import Survey
from survey.decorators import survey_available
from survey.forms import ResponseForm

LOGGER = logging.getLogger(__name__)


class IndexView(survey_views.IndexView):
    template_name = "starting_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["survey"] = Survey.objects.all()[0]

        return context


class SurveyDetail(survey_views.SurveyDetail):
    @survey_available
    def get(self, request, *args, **kwargs):
        survey = kwargs.get("survey")
        step = kwargs.get("step", 0)
        template_name = "question_page.html"

        form = ResponseForm(survey=survey, user=request.user, step=step)
        categories = form.current_categories()

        asset_context = {
            "flatpickr": any(
                [
                    field.widget.attrs.get("class") == "date"
                    for _, field in form.fields.items()
                ]
            )
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
