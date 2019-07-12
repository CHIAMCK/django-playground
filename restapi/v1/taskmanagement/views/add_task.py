from rest_framework.generics import CreateAPIView
from ..serializers import TaskSerializer
from taskmanagement.models import Task
from rest_framework.permissions import IsAuthenticated
from restapi.v1.mixin import CsrfExemptSessionAuthentication


class TaskAddView(CreateAPIView):
    # CreateAPIVIEW Used for create-only endpoints.
    authentication_classes = [CsrfExemptSessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
