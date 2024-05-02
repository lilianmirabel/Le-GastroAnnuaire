from restaurant.models import Restaurant, TypeResto, Commentaire
from django.forms import ModelChoiceField

from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from .models import TypeResto

class ajoutTypeRestaurantForm(forms.ModelForm):
    class Meta:
        model = TypeResto
        fields = ['nomType']
        labels = {'nomType': 'Nom du type de restaurant'}
        help_texts = {'nomType': 'Entrez le nom du type de restaurant'}
        error_messages = {'nomType': {'required': 'Ce champ est obligatoire'}}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Fieldset(
                'Ajouter un type de restaurant',
                'nomType',
            ),
            ButtonHolder(
                Submit('submit', 'Ajouter', css_class='btn btn-primary')
            )
        )