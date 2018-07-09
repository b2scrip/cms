from django import forms
from .models import Profile

class JoinForm(forms.Form): # or forms.ModelForm
    email = forms.EmailField()
    name = forms.CharField(max_length=120)
    def clean_email(self):
        email = self.cleaned_data["email"]
        if "gmail" in email:
            raise forms.ValidationError("gmail is not allow to register")
        return email
        
class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["bio","picture"]
