from django.urls import path, include
from rest_framework.routers import DefaultRouter
from questions.api.views import QuestionViewSet, AnswerCreateAPIView, QuestionAnswersListAPIView

router = DefaultRouter()
router.register(r'questions', QuestionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('questions/<slug:slug>/answers/', QuestionAnswersListAPIView.as_view(), name='answer_list'),
    path('questions/<slug:slug>/answer/', AnswerCreateAPIView.as_view(), name='create_answer'),
]
