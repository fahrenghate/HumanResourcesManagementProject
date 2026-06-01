from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        widgets = {
            'fullname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Иванов Иван Иванович'}),
            'position': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Разработчик'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+79991234567'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'test@mail.ru'}),
            'salary': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '80000'}),
            'department': forms.Select(attrs={'class': 'form-select'}),
        }