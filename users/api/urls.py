from django.urls import path
from users.api.views import CurrentUserAPIView

urlpatterns = [
    path('', CurrentUserAPIView.as_view(), name='current_user')
]
