from django.forms import ModelForm
from . models import Profile

class ProfileForm(ModelForm):
    class Meta:
        # adding profile from the model to the model
        model = Profile
        # excluding the uuid field
        exclude = ['uuid']

        # so in this we are asking every things form profile model but excluding uuid 