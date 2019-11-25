from django import forms
from taskmanagement.models import Task
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Layout


class AddTaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = [
            'title',
            'description',
            'assigned_to'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        # self.helper.layout = Layout(
        #     Div(
        #         Div(css_class='col-sm-3 d-xs-none'),
        #         css_class='row',
        #     )
        # )
