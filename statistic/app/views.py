from django.shortcuts import render
from django.views.generic import TemplateView
from .mixins import QuizStatisticsMixin
from .models import *


class YourQuizView(QuizStatisticsMixin, TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['questions'] = Questions.objects.all()


        user = self.request.user
        context['user_answers'] = Journal.objects.filter(user=user, correct_answers_count__gt=0)
        return context
