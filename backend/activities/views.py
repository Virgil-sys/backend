from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Activity, BookingActivity
from .serializers import ActivitySerializer, BookingActivitySerializer


class ActivityViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint for browsing available activities, transport, and accommodation
    """
    queryset = Activity.objects.filter(is_active=True)
    serializer_class = ActivitySerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description', 'activity_id']
    ordering_fields = ['price', 'title', 'display_order']
    ordering = ['category', 'display_order', 'title']
    
    @action(detail=False, methods=['get'])
    def by_category(self, request):
        """Get activities grouped by category"""
        category = request.query_params.get('category', None)
        
        if category:
            activities = self.queryset.filter(category=category)
        else:
            activities = self.queryset
        
        serializer = self.get_serializer(activities, many=True)
        return Response(serializer.data)
