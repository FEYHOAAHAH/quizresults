from django.db.models import Sum
from .models import Journal


class QuizStatisticsMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = self.request.user
        quizzes_taken = Journal.objects.filter(user=user).count()

        # Use correct_answers_count and incorrect_answers_count directly
        correct_answers = \
            Journal.objects.filter(user=user, correct_answers_count__gt=0).aggregate(Sum('correct_answers_count'))[
                'correct_answers_count__sum'] or 0
        incorrect_answers = \
            Journal.objects.filter(user=user, incorrect_answers_count__gt=0).aggregate(Sum('incorrect_answers_count'))[
                'incorrect_answers_count__sum'] or 0

        context['quizzes_taken'] = quizzes_taken
        context['correct_answers'] = correct_answers
        context['incorrect_answers'] = incorrect_answers

        return context
