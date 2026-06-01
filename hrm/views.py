import csv
from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Employee
from .forms import EmployeeForm

class EmployeeListView(ListView):
    model = Employee
    template_name = 'hrm/employee_list.html'
    context_object_name = 'employees'

class EmployeeCreateView(LoginRequiredMixin, CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'hrm/employee_form.html'
    success_url = reverse_lazy('employee_list')

class EmployeeUpdateView(LoginRequiredMixin, UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'hrm/employee_form.html'
    success_url = reverse_lazy('employee_list')

class EmployeeDeleteView(LoginRequiredMixin, DeleteView):
    model = Employee
    template_name = 'hrm/employee_confirm_delete.html'
    success_url = reverse_lazy('employee_list')

@login_required
def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="employees.csv"'
    response.write(u'\ufeff'.encode('utf8')) # Поддержка русского языка в Excel
    writer = csv.writer(response, delimiter=';')
    writer.writerow(['ФИО', 'Должность', 'Телефон', 'Email', 'Зарплата', 'Отдел'])
    
    for emp in Employee.objects.all():
        writer.writerow([emp.fullname, emp.position, emp.phone, emp.email, emp.salary, emp.department.name])
    return response