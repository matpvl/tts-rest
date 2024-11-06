from django.urls import path

from .views import TicketListView, TicketDetailView

urlpatterns = [
    # LIST , POST
    path("tickets/", TicketListView.as_view(), name="ticket-list"),
    # GET, PUT, PATCH, DELETE
    path("tickets/<int:id>/", TicketDetailView.as_view(), name="ticket-detail"),
]
