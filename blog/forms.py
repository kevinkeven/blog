from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Comment
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Submit
from crispy_forms.bootstrap import InlineRadios, InlineField

class EmailPostShare(forms.Form):
    name = forms.CharField(max_length=30, label='Your name')
    email = forms.EmailField(label='Email Address')
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(EmailPostShare, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-control'
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md-6 mb-0'),
                Column('email', css_class='form-group col-md-6 mb-0'),
            ),
            'to',
            'comments',
            Submit('submit', 'Send', css_class='btn btn-block btn-primary')
        )

class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-control'
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md-6 mb-0'),
                Column('email', css_class='form-group col-md-6 mb-0'),
            ),
            'body',
            Submit('submit', 'Add comment', css_class='btn btn-block btn-primary')
        )

    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
        labels = {
            'name': _('Your name'),
            'email': _('Your Email Address'),
            'body': _('Your Comment')
        }
        

class SearchForm(forms.Form):
    query = forms.CharField(label='Search Here')

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'inlineFormInputGroupUsername'
        self.helper.form_class = 'form-control'

class FeedbackForm(forms.Form):
    name = forms.CharField(max_length=30, label='Your name')
    email = forms.EmailField(label='Email Address')
    subject = forms.CharField(max_length=180)
    message = forms.CharField(widget=forms.Textarea)
    

    def __init__(self, *args, **kwargs):
        super(FeedbackForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form_control'
        self.helper.layout = Layout(

            Row(
                Column('name', css_class='form-group col-md-6 mb-0'),
                Column('email', css_class='form-group col-md-6 mb-0'), 
            ),                                                       
            'subject',
            'message',
            Submit('submit', 'Send', css_class='btn btn-block btn-primary')
        )
        