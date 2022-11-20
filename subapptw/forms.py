from django.forms import ModelForm
from .models import Twitter

class TwitterForm(ModelForm):
    class Meta:
        model =  Twitter
        fields = '__all__'
