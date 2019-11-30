from django import forms
from taskmanagement.models import Task
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Layout
from utils.forms.layout import FormCard, CreateSubmitButtons


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

        fields = ['title', 'description', 'assigned_to']

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Div(css_class='col-sm-3 d-xs-none'),
                FormCard('Task details', fields, icon='queue'),
                css_class='row',
            ),
            Div(
                Div(css_class='col-sm-3 d-xs-none'),
                Div(CreateSubmitButtons(), css_class='col-sm-6 col-xs-12'),
                css_class='row',
            ),
        )
