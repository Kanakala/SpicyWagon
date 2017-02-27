from django import forms
from django.forms import ModelForm, CharField, TextInput
from registration.forms import RegistrationForm
from django.utils.translation import ugettext_lazy as _
from custom_user.models import EmailUser
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from phonenumber_field.formfields import PhoneNumberField
from localflavor.in_.forms import INPhoneNumberField
import localflavor
class EmailUserCreationForm(RegistrationForm):

    """A form for creating new users.

    Includes all the required fields, plus a repeated password.

    """

    error_messages = {
        'duplicate_email': _("A user with that email already exists."),
        'password_mismatch': _("The two password fields didn't match."),
    }
    name = forms.CharField(
        label=_("Your Name"),
        widget=forms.TextInput)
    email = forms.CharField(
        label=_("Email Address"),
        widget=forms.EmailInput)
    username = CharField( widget=TextInput(attrs={'type':'number'}),
        label=_("Phone Number"),
        )
    password = forms.CharField(
        label=_("Password"),
        widget=forms.PasswordInput)
    CHOICES= (('Partner', 'Partner'),('Customer', 'Customer'),)
    Label = forms.ChoiceField(choices=CHOICES, label='Label', widget=forms.RadioSelect())
   

    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'name', 'password', 'Label',)
	
    def __init__(self, *args, **kwargs):
        super(EmailUserCreationForm, self).__init__(*args, **kwargs)
        self.fields.keyOrder = ['email', 'username', 'name', 'password', 'Label']

    def clean_email(self):
        """Clean form email.

        :return str email: cleaned email
        :raise forms.ValidationError: Email is duplicated

        """
        # Since EmailUser.email is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        email = self.cleaned_data["email"]
        try:
            get_user_model()._default_manager.get(email=email)
        except get_user_model().DoesNotExist:
            return email
        raise forms.ValidationError(
            self.error_messages['duplicate_email'],
            code='duplicate_email',
        )

    

    def save(self, commit=True):
        """Save user.

        Save the provided password in hashed format.

        :return custom_user.models.EmailUser: user

        """
        user = super(EmailUserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class EmailUserChangeForm(forms.ModelForm):

    """A form for updating users.

    Includes all the fields on the user, but replaces the password field
    with admin's password hash display field.

    """

    username = CharField( widget=TextInput(attrs={'type':'number'}),label=_("Phone Number"))
    password = ReadOnlyPasswordHashField(label=_("Password"), help_text=_(
        "Raw passwords are not stored, so there is no way to see "
        "this user's password, but you can change the password "
        "using <a href=\"password/\">this form</a>."))
    

    class Meta:
        model = get_user_model()
        exclude = ()

    def __init__(self, *args, **kwargs):
        """Init the form."""
        super(EmailUserChangeForm, self).__init__(*args, **kwargs)
        f = self.fields.get('user_permissions', None)
        if f is not None:
            f.queryset = f.queryset.select_related('content_type')

    def clean_password(self):
        """Clean password.

        Regardless of what the user provides, return the initial value.
        This is done here, rather than on the field, because the
        field does not have access to the initial value.

        :return str password:

        """
        return self.initial["password"]
	
