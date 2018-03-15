from django import forms
from .models import Files

#For Class Meta it links back to the mode check the model to make changes.
class FileForm(forms.ModelForm):
    class Meta:
        model = Files
        fields = ('description', 'video', )
