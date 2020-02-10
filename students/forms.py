from courses.models import Course
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CourseEnrollForm(forms.Form):
    course=forms.ModelChoiceField(queryset=Course.objects.all(),widget=forms.HiddenInput)

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)
    town=forms.CharField(max_length=60)

    class Meta:
        model = User
        fields = ("username", "email","town", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user