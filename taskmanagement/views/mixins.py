from ..models import Task

# class SubmitButtonsMixin:

#     def __init__(self, *args, **kwargs):
#         if not self.prefix:
#             raise ImproperlyConfigured(
#                 'Prefix is required'
#             )
#         super().__init__(*args, **kwargs)

#     def get_success_url(self, *args, **kwargs):

#         if 'save_add' in self.request.POST:

#         return reverse(f'{self.prefix}:{suffix}')


class RestrictTaskListMixin:
    def get_queryset(self):
        user = self.request.user
        # handle if queryset is not provided
        try:
            qs = super().get_queryset()
        except AttributeError:
            qs = Task.objects

        qs = qs.filter(assigned_to=user)
        return qs
