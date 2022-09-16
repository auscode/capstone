from django.forms import ModelForm
from . models import Profile

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        # excluding the uuid field
        exclude = ['uuid']