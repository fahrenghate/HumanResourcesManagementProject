from django.db import models
from django.core.validators import RegexValidator

class Department(models.Model):
    name = models.CharField("Наименование отдела", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Отдел"
        verbose_name_plural = "Отделы"

class Employee(models.Model):
    phone_regex = RegexValidator(regex=r'^\+7\d{10}$', message="Формат телефона: '+79991234567'.")
    
    fullname = models.CharField("ФИО", max_length=150)
    position = models.CharField("Должность", max_length=100)
    phone = models.CharField("Телефон", validators=[phone_regex], max_length=12)
    email = models.EmailField("Email", unique=True)
    salary = models.DecimalField("Зарплата", max_digits=10, decimal_places=2)
    department = models.ForeignKey(Department, on_delete=models.PROTECT, verbose_name="Отдел")

    def __str__(self):
        return f"{self.fullname} — {self.position}"

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"