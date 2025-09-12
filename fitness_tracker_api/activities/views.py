from rest_framework import viewsets, permissions, generics
from .models import Activity
from .serializers import ActivitySerializer, UserSerializer
from django.contrib.auth.models import User


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Only return activities of the logged-in user
        return Activity.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Automatically set the logged-in user as the activity owner
        serializer.save(user=self.request.user)


# ✅ User Registration API
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
