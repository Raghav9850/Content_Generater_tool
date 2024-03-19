from django import forms

class InputForm(forms.Form):
    user_input = forms.CharField(label='User Input', widget=forms.Textarea)