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
