from django.urls import path, include
from rest_framework.routers import DefaultRouter
from questions.api import views as qv

router = DefaultRouter()
router.register(r'questions', qv.QuestionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('questions/<slug:slug>/answers/', qv.QuestionAnswersListAPIView.as_view(), name='answer_list'),
    path('questions/<slug:slug>/answer/', qv.AnswerCreateAPIView.as_view(), name='answer_create'),
    path('answers/<int:pk>/', qv.AnswerRUDAPIView.as_view(), name='answer_detail'),
    path('answers/<int:pk>/like', qv.AnswerLikeAPIView.as_view(), name='answer_like'),
]
