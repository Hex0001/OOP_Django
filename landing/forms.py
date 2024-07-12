from django import forms


class TemplateForm(forms.Form):
    patient_name = forms.CharField()
    doctor_name = forms.ChoiceField(choices=(
        ("ivanov", "Иванов"),
        ("petrov", "Петров"),
        ("sidorov", "Сидоров")
    ))
    department = forms.ChoiceField(choices=(
        ("stomatology", "Стоматология"),
        ("hirurgy", "Хирургия"),
        ("neuropatology", "Невропатология")
    ))
    phone_number = forms.RegexField(regex=r"(\+7|8)[\s(]*\d{3}[)\s]*\d{3}[\s-]?\d{2}[\s-]?\d{2}")
    symptoms = forms.CharField()
    date = forms.DateField()
    ip = forms.CharField()
    user_agent = forms.CharField()


class ContactForm(forms.Form):
    fullname = forms.CharField()
    contact_email = forms.EmailField()
    contact_number = forms.RegexField(regex=r"(\+7|8)[\s(]*\d{3}[)\s]*\d{3}[\s-]?\d{2}[\s-]?\d{2}")
    contact_msg = forms.CharField(widget=forms.Textarea)
    ip = forms.CharField()
    user_agent = forms.CharField()
