from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=30, label='主题')
    email = forms.EmailField(required=False, label='e-mail')
    message = forms.CharField(max_length=300, widget=forms.Textarea)

    def clean_message(self):
        message = self.cleaned_data['message']
        num_words = len(message.split())
        if num_words < 4:
            raise forms.ValidationError("Not enough words!")
        return message