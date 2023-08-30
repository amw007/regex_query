from django import forms


class RegexForm(forms.Form):
    input_string = forms.CharField(label="Enter String")
    input_regex = forms.CharField(label="Enter regex")
