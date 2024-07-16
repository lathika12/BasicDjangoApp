from django import forms
from BasicUserCRUD import models


class UserForm(forms.ModelForm):
    class Meta:
        model = models.UserProfile
        fields = '__all__'
