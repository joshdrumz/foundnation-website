from django import forms


def should_be_empty(value):
    if value:
        raise forms.ValidationError('Field is not empty')


class ContactForm(forms.Form):
    name = forms.CharField(max_length=80, widget=forms.TextInput(
        attrs={'placeholder': 'Your Name', 'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'placeholder': 'Your Email', 'class': 'form-control'}))
    subject = forms.CharField(max_length=80, widget=forms.TextInput(
        attrs={'placeholder': 'Your Subject', 'class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'Your Message', 'class': 'form-control'}))
    forcefield = forms.CharField(
        required=False, widget=forms.HiddenInput, label='Leave empty', validators=[should_be_empty])
