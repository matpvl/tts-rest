from rest_framework import mixins, generics
from tickets.models import Ticket
from .serializers import TicketSerializer


class TicketListView(
    mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView
):
    """View for listing and creating tickets"""

    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    def get(self, request, *args, **kwargs):
        """Handle GET requests for listing tickets"""
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """Handle POST requests for creating tickets"""
        return self.create(request, *args, **kwargs)


class TicketDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView,
):
    """View for retrieving, updating, and deleting a specific ticket"""

    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    lookup_field = "id"

    def get(self, request, *args, **kwargs):
        """Handle GET requests for retrieving a specific ticket"""
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """Handle PUT requests for full updates of a specific ticket"""
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        """Handle PATCH requests for partial updates of a specific ticket"""
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """Handle DELETE requests for deleting a specific ticket"""
        return self.destroy(request, *args, **kwargs)
