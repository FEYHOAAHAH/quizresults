from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Journal, Questions, UserAnswer


@receiver(post_save, sender=UserAnswer)
def save_test_results(sender, instance, created, **kwargs):
    if created:
        user = instance.user
        question = instance.question
        correct_answers_count = instance.is_correct
        incorrect_answers_count = not instance.is_correct

        Journal.objects.create(
            user=user,
            question=question,
            correct_answers_count=correct_answers_count,
            incorrect_answers_count=incorrect_answers_count
        )
