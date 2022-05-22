from django.forms import ModelForm, TextInput
from .models import Imprint

class ImprintForm(ModelForm):
    class Meta:
        model = Imprint
        fields = '__all__'
        widgets = {
            'authors': TextInput(attrs={
                'class': "form-control",
                # 'style': 'max-width: 300px;',
                'style': 'height:60px;',
                'placeholder': 'Authors'
                }),
        }