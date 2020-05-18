from django import forms
from .models import Branches, Department, Employee, ITService, ServiceType, PaymentMethod, Equipment, Client, Order, Stock, Provider, Post, Contract
from django.forms import SelectDateWidget
from django.contrib.admin.widgets import AdminDateWidget

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

from django.contrib.auth.models import User

class UserRegistrationForm(forms.ModelForm):
        password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
        password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)

        class Meta:
            model = User
            fields = ('username', 'email')

        def clean_password2(self):
            cd = self.cleaned_data
            if cd['password'] != cd['password2']:
                raise forms.ValidationError('Пароли не совпадают')
            return cd['password2']

class BranchForm(forms.ModelForm):
    class Meta:
        model=Branches
        fields=('BranchName','BranchPhone', 'BranchAddress')

class DepartmentForm(forms.ModelForm):
    class Meta:
        model=Department
        fields=('DepartmentNumber', 'DepartmentName', 'Branch')

class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields=('EmpName', 'EmpSurname', 'EmpPatronymic','Post','EmpPhone', 'EmpEmail', 'Department')

class StockForm(forms.ModelForm):
    class Meta:
        model=Stock
        fields=('StockAddress', 'StockPhone')

class ITServiceForm(forms.ModelForm):
    class Meta:
        model=ITService
        fields=('ServiceName', 'ServiceType', 'ServicePrice','ServiceDescription','ServiceGaurantee','ServicePeriod', 'ServiceAvailable','Equipments')

class FilterForm(forms.Form):
    min_price = forms.FloatField(label='От', required=False)
    max_price = forms.FloatField(label='До', required=False)

#class OrderSearch(forms.Form):
 #   status_choices = (('Создан', 'Создан'), ('Обрабатывается', 'Обрабатывается'), ('Выполнен', 'Выполнен'))
  #  status = forms.CharField(max_length=50, label='Статус заказа', choices=status_choices,)

class OrderSearch(forms.Form):
    status_choices = (('Создан', 'Создан'), ('Обрабатывается', 'Обрабатывается'), ('Выполнен', 'Выполнен'))
    OrderStatus=forms.ChoiceField(label='Статус заказа',widget=forms.RadioSelect, choices=status_choices, required=False)


class EquipmentForm(forms.ModelForm):
    class Meta:
        model=Equipment
        fields=('EquipmentName', 'EquipmentQuantity', 'Stock', 'Provider')

class ClientForm(forms.ModelForm):
    class Meta:
        model=Client
        fields=('ClientName', 'ClientSurname', 'ClientPatronymic', 'ClientPhone', 'ClientEmail')

class EmpClientForm(forms.ModelForm):
    class Meta:
        model=Client
        fields=('ClientName', 'ClientSurname', 'ClientPatronymic', 'ClientPhone', 'ClientEmail', 'User')


class OrderForm(forms.ModelForm):
    class Meta:
        model=Order
        fields=('OrderRequirement','ITService', 'PaymentMethod')

class EmpOrderForm(forms.ModelForm):
    class Meta:
        model=Order
        fields=('Client','OrderRequirement','ITService','PaymentMethod','OrderDate','OrderStatus', 'Employee')
        widgets={'OrderDate':AdminDateWidget}

class ProviderForm(forms.ModelForm):
    class Meta:
        model=Provider
        fields=('ProviderName','ProviderPhone', 'ProviderEmail')

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('PostName','PostSalary')

class ServiceTypeForm(forms.ModelForm):
    class Meta:
        model=ServiceType
        fields=('TypeName','TypeDescription', 'image')

class PaymentMethodForm(forms.ModelForm):
    class Meta:
        model=PaymentMethod
        fields=('PaymentType','PaymentName')


class ContractForm(forms.ModelForm):
    class Meta:
        model=Contract
        fields=('ContractNumber','Order', 'ContractDate', 'ContractEndDate')
        widgets={'ContractDate': AdminDateWidget, 'ContractEndDate': AdminDateWidget}


class ContractSearchForm(forms.Form):
    date1=forms.DateField(label='От', required=False, widget=AdminDateWidget)
    date2=forms.DateField(label='до', required=False, widget=AdminDateWidget)
