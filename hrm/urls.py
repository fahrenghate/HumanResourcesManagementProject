from django.urls import path
from . import views

urlpatterns = [
    path('', views.EmployeeListView.as_view(), name='employee_list'),
    path('add/', views.EmployeeCreateView.as_view(), name='employee_add'),
    path('edit/<int:pk>/', views.EmployeeUpdateView.as_view(), name='employee_edit'),
    path('delete/<int:pk>/', views.EmployeeDeleteView.as_view(), name='employee_delete'),
    path('export/', views.export_csv, name='export_csv'),
]