from rest_framework import serializers
from tickets.models import Ticket


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = [
            "id",
            "title",
            "description",
            "priority",
            "category",
            "status",
            "issuer",
            "assignee",
            "created_at",
            "updated_at",
            "due_date",
            "upvotes",
            "downvotes",
            "hidden",
        ]
