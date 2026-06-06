from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from captcha.fields import CaptchaField

class CustomLoginForm(AuthenticationForm):
    captcha = CaptchaField()

class AnketForm(UserCreationForm):
    photo = forms.ImageField(required=True)
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=15, required=True,initial='+996')
    gender = forms.CharField(max_length=10, required=True)
    previous_experience = forms.CharField(max_length=200, required=True)
    recommendation = forms.CharField(max_length=200, required=True)
    reason_to_join = forms.CharField(max_length=200, required=True)
    hours_per_week = forms.IntegerField(required=True)
    satisfaction_level = forms.IntegerField(required=True)

    class Meta:
        model = models.Anket
        fields = ('username',
                  'password1',
                  'password2',
                  'photo',
                  'email',
                  'phone_number',
                  'gender',
                  'previous_experience',
                  'recommendation',
                  'reason_to_join',
                  'hours_per_week',
                  'satisfaction_level',
                )
    def save(self, commit=True):
        user = super(AnketForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user