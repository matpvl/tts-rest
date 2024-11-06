from rest_framework import mixins, generics
from tickets.models import Ticket
from .serializers import TicketSerializer


# View for listing and retrieving tickets
class TicketListView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    # Handle GET requests for listing tickets
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class TicketDetailView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    lookup_field = "id"

    # Handle GET requests for retrieving a specific ticket
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
