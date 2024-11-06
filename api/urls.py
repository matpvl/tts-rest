from django.urls import path
from .views import TicketListView, TicketDetailView

urlpatterns = [
    path("tickets/", TicketListView.as_view(), name="ticket-list"),
    path("tickets/<int:id>/", TicketDetailView.as_view(), name="ticket-detail"),
]
