from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field

class RegisterForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.form_action = '.'
        self.helper.add_input(Submit('Submit', 'Submit', css_class='btn-primary'))

    username = forms.CharField(label="Username", required=True)
    email = forms.CharField(label="Email", required=True)
    password = forms.CharField(
        label="Password", required=True, widget=forms.PasswordInput)

class LoginForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('login', 'login', css_class='btn-primary'))

    username = forms.CharField(label="Username", required=True)
    password = forms.CharField(
        label="Password", required=True, widget=forms.PasswordInput)