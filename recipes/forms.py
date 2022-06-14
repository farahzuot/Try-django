from django import forms
from .models import Recipe, RecipeIngredient

class RecipeForm(forms.ModelForm):
    # django-crispy-forms >> library to do this work and clean up the form.
    error_css_class = 'error-field'
    required_css_class = 'required-field'
    name = forms.CharField(help_text='This is your help! <a href="/contact-us">Contact Us</a>')
    class Meta:
        model = Recipe
        fields = ['name', 'description' , 'directions']

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[str(field)].widget.attrs.update({
                'placeholder':f'Recipe {str(field)}',
                'class':'form-control'
            }) 
            # self.fields[str(field)].label=''
        self.fields['description'].widget.attrs.update({'rows':'2'}) 
        self.fields['directions'].widget.attrs.update({'rows':'4'}) 



class RecipeIngredientForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = ['name', 'quantity' , 'unit']
