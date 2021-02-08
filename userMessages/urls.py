from django.urls import path
from .views import messages_view
urlpatterns = [
    path('view/', messages_view),
]