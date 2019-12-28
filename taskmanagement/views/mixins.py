

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
