
# we can override get_form_kwargs() method to pass request to the form
# get_form_kwargs() is used to build the keyword arguments required to instantiate the form
class PassRequestToFormView:
    def get_Form_kwargs(self):
        kwargs = super().get_form_kwargs()
