# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group, User

admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.register(QuestionPage)
admin.site.register(FillInQuestion)
admin.site.register(MultipleChoiceQuesition)
admin.site.register(MultipleSelectQuestion)
