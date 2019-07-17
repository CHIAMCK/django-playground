from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from restapi.v1.mixin import CsrfExemptSessionAuthentication
from taskmanagement.models import Task

from ..serializers import TaskSerializer


class TaskAddView(CreateAPIView):
    # CreateAPIVIEW Used for create-only endpoints.
    # Provides a post method handler.
    authentication_classes = [CsrfExemptSessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
