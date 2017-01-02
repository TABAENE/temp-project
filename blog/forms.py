from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class BlogForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-inline'
        self.helper.form_method = 'POST'
        self.helper.form_action = '.'
        self.helper.add_input(Submit('Post', 'Post', css_class='btn-primary'))

    comment = forms.CharField(label="Comment", max_length=600,
                              widget=forms.Textarea(attrs={
                                  'cols': 20, 'rows': 5,
                                  'data-limit': 600
                              }), required=True)

    # TabHolder(
    #     Tab('Python blog',
    #         'field_name_1',
    #         Div('field_name_2')
    #     ),
    #     Tab('Django Blog',
    #         Field('field_name_3', css_class="extra")
    #     )
    # )