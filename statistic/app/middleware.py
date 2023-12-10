from .models import Questions

class QuestionViewsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Check if the response has a Question object
        if hasattr(request, 'question'):
            question = request.question
            question.views += 1
            question.save()

        return response