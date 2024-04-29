from django.core import validators
from django import forms
from .models import User,Address
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""

    password1 = forms.CharField(label="گذرواژه", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="تکرار گذرواژه", widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ["phone"]

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ["phone", "password", "is_active", "is_admin"]


# def start_with_0(value):
#     if value[0] != '0':
#         raise forms.ValidationError("number shuld start with 0 ")


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', "placeholder": "your username"}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', "placeholder": "Your password"}))

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if len(username) > 500:
            raise ValidationError(
                "invalid value:%(value)s is invalid",
                code="invalid",
                params={"value": f"{username}"}
            )
        return username

    # def clean(self):
    #     cd=super().clean()
    #     phone = cd["phone"]
    #     if len(phone) > 11:
    #         raise ValidationError(
    #             "invalid value:%(value)s is invalid clean",
    #             code="invalid",
    #             params={"value":f"{phone}"}
    #         )


class RegisterForm(forms.Form):
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', "placeholder": "Your phone number"}),
                            validators=[validators.MaxLengthValidator(11)])
class CheckOtpForm(forms.Form):
    code = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', "placeholder": "enter the code"}),
                            validators=[validators.MaxLengthValidator(4)])


class AddressCreationForm(forms.ModelForm):
    user=forms.IntegerField(required=False)
    class Meta:
        model=Address
        exclude="__all__"