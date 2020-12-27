# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.models import Group, User
from survey.models import Answer, Category, Question, Response, Survey
from survey import admin as survey_admin


admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.unregister(Survey)
admin.site.unregister(Response)


class QuestionInline(survey_admin.QuestionInline):
    verbose_name = "Intrebare"
    verbose_name_plural = "Intrebari"

    def get_formset(self, request, survey_obj, *args, **kwargs):
        formset = super(QuestionInline, self).get_formset(request, survey_obj, *args, **kwargs)
        if survey_obj:
            formset.form.base_fields["category"].queryset = survey_obj.categories.all()
            formset.form.base_fields["category"].label = 'Pagina'
            formset.form.base_fields["type"].label = 'Tipul'
            formset.form.base_fields["choices"].label = 'Optinui'
            formset.form.base_fields["required"].label = 'Raspuns obligatoriu'
            formset.form.base_fields["order"].label = 'Ordinea in pagina'

        return formset


class CategoryInline(survey_admin.CategoryInline):
    verbose_name = "Pagina de intrebari"
    verbose_name_plural = "Pagini de intrebari"


class SurveyAdmin(survey_admin.SurveyAdmin):
    list_display = ("name",)
    exclude = ("publish_date", "expire_date", "template", "editable_answers", "display_method", "need_logged_user", "is_published")
    inlines = [CategoryInline, QuestionInline]

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class ResponseAdmin(admin.ModelAdmin):
    list_display = ("interview_uuid", "created")


admin.site.register(Survey, SurveyAdmin)
admin.site.register(Response, ResponseAdmin)