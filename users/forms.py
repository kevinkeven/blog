from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Profile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Submit
from crispy_forms.bootstrap import InlineRadios, InlineField
from django.utils.translation import gettext_lazy as _

class CustomUserCreationForm(UserCreationForm, forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.use_custom_control = True
        self.helper.layout = Layout(
            'username',
            Row(
                Column('first_name', css_class='form-group col-md-6 mb-0'),
                Column('last_name', css_class='form-group col-md-6 mb-0'),
            ),
            'email',
            'age',
            'password1',
            'password2',
            Submit('submit', 'Create Account', css_class='btn btn-dark btn-block')
            )

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'age', 'password1', 'password2')

class CustomUserChangeForm(UserChangeForm):
    
    def __init__(self, *args, **kwargs):
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.use_custom_control = True
        self.helper.layout = Layout(
            Row(
                Column('first_name', css_class='form-group col-md-6 mb-0'),
                Column('last_name', css_class='form-group col-md-6 mb-0'),
            ),
            'email',
            'age',
            Submit('submit', 'Save', css_class='btn btn-dark')
            )

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'age')

class ProfileForm(forms.ModelForm):
    owner = forms.ModelChoiceField(
        widget = forms.HiddenInput,
        queryset = CustomUser.objects.all(),
        disabled = True,
        required = False,
    )

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.use_custom_control = True
        self.helper.layout = Layout(
            'owner',
            'bio',
            'location',
            Row(
                Column('fa_account', css_class='form-group col-md-6 mb-0'),
                Column('tw_account', css_class='form-group col-md-6 mb-0'),
            ),
            Row(
                Column('in_account', css_class='form-group col-md-6 mb-0'),
                Column('li_account', css_class='form-group col-md-6 mb-0'),
            ),
            Submit('submit', 'Save', css_class='btn btn-dark btn-block'),
            )
    
    class Meta:
        model = Profile
        fields = ('owner', 'bio', 'location', 'fa_account', 'tw_account', 'in_account', 'li_account')

class ProfileUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.use_custom_control = True
        self.helper.layout = Layout(
            'owner',
            'avatar'
            'bio',
            'location',
            Row(
                Column('fa_account', css_class='form-group col-md-6 mb-0'),
                Column('tw_account', css_class='form-group col-md-6 mb-0'),
            ),
            Row(
                Column('in_account', css_class='form-group col-md-6 mb-0'),
                Column('li_account', css_class='form-group col-md-6 mb-0'),
            ),
            Submit('submit', 'Save', css_class='btn btn-dark btn-block')
            )
    
    class Meta:
        model = Profile
        fields = ('owner', 'avatar', 'bio', 'location', 'fa_account', 'tw_account', 'in_account', 'li_account')