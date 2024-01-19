from django import forms
from service_app.models import ServiceModel

class BrandForm(forms.ModelForm):
    class Meta:
        model = ServiceModel
        fields = '__all__'