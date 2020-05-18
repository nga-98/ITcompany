from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.
class Branches(models.Model):
    BranchName=models.CharField(max_length=200, verbose_name='Название филиала')
    BranchPhone=models.CharField(max_length=20, verbose_name='Телефон филиала')
    BranchAddress=models.TextField(verbose_name='Адрес филиала')
    class Meta:
        verbose_name='Филиал'
        verbose_name_plural='Филиалы'
    def __str__(self):
        return self.BranchName

class Department(models.Model):
    DepartmentNumber=models.IntegerField(verbose_name='Номер отдела')
    Branch=models.ForeignKey(Branches, on_delete=models.CASCADE, verbose_name='Филиал')
    DepartmentName=models.CharField(max_length=200, verbose_name='Название отдела')
    class Meta:
        verbose_name='Отдел'
        verbose_name_plural='Отделы'
    def __str__(self):
        return self.DepartmentName

class Post(models.Model):
    PostName=models.CharField(max_length=200, verbose_name='Название должности')
    PostSalary=models.FloatField(verbose_name='Оклад')
    class Meta:
        verbose_name='Должность'
        verbose_name_plural='Должности'
    def __str__(self):
        return self.PostName

class Employee (models.Model):
    EmpName=models.CharField(max_length=100, verbose_name='Имя')
    EmpSurname=models.CharField(max_length=100, verbose_name='Фамилия')
    EmpPatronymic=models.CharField(max_length=100, verbose_name='Отчество')
    Post=models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Должность')
    EmpPhone=models.CharField(max_length=20, verbose_name='Телефон')
    EmpEmail=models.EmailField(max_length=50, verbose_name='E-mail')
    Department=models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name='Отдел')
    class Meta:
        verbose_name='Сотрудник'
        verbose_name_plural='Сотрудники'
    def __str__(self):
        return '%s %s %s'%(self.EmpSurname,self.EmpName, self.EmpPatronymic)

class ServiceType(models.Model):
    TypeName=models.CharField(max_length=200, verbose_name='Название типа')
    TypeDescription=models.TextField(verbose_name='Описание типа')
    slug = models.SlugField(max_length=200, db_index=True,unique=True)
    image=models.ImageField(blank=True, null=True, upload_to='photo/', verbose_name='Изображение')
    class Meta:
        verbose_name='Тип услуги'
        verbose_name_plural='Типы услуг'
    def __str__(self):
        return self.TypeName
    def get_absolute_url(self):
        return reverse('service_list_by_category',
                        args=[self.slug])

class Stock(models.Model):
    StockAddress=models.TextField(verbose_name='Адрес склада')
    StockPhone=models.CharField(max_length=20, verbose_name='Телефон склада')
    class Meta:
        verbose_name='Склад'
        verbose_name_plural='Склады'
    def __str__(self):
        return self.StockAddress

class Provider(models.Model):
    ProviderName=models.CharField(max_length=200, verbose_name='Наименование поставщика')
    ProviderPhone=models.CharField(max_length=20, verbose_name='Телефон поставщика')
    ProviderEmail=models.CharField(max_length=50, verbose_name='E-mail поставщика')
    class Meta:
        verbose_name='Поставщик'
        verbose_name_plural='Поставщики'
    def __str__(self):
        return self.ProviderName

class Equipment(models.Model):
    EquipmentName=models.CharField(max_length=200, verbose_name='Название')
    EquipmentQuantity=models.IntegerField(verbose_name='Количество')
    Stock=models.ForeignKey(Stock, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Склад')
    Provider=models.ForeignKey(Provider, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Поставщик')
    class Meta:
        verbose_name='Оборудование'
        verbose_name_plural='Оборудование'
    def __str__(self):
        return self.EquipmentName

from django.core.validators import MinValueValidator
class ITService (models.Model):
    ServiceName=models.CharField(max_length=200, verbose_name='Название услуги')
    ServiceType=models.ForeignKey(ServiceType, on_delete=models.CASCADE, verbose_name='Тип услуги')
    ServicePrice=models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Цена услуги', validators=[MinValueValidator(0.01)])
    ServiceDescription=models.TextField(verbose_name='Описание услуги')
    gaurantee_choices=(('6 месяцев','6 месяцев'),('12 месяцев','12 месяцев'),('24 месяца','24 месяца'), ('36 месяцев', '36 месяцев'))
    ServiceGaurantee=models.CharField(max_length=100, choices=gaurantee_choices, verbose_name='Срок гарантии')
    period_choices=(('1 месяц', '1 месяц'), ('2 месяца', '2 месяца'), ('3 месяца', '3 месяца'), ('6 месяцев','6 месяцев'))
    ServicePeriod = models.CharField(blank=True, null=True,max_length=100,choices=period_choices, verbose_name='Период предоставления услуги')
    ServiceAvailable = models.BooleanField(default=True, verbose_name='Предоставляется?')
    Equipments=models.ManyToManyField(Equipment, verbose_name='Необходимое оборудование')
    class Meta:
        verbose_name='IT-услуга'
        verbose_name_plural='IT-услуги'
    def __str__(self):
        return self.ServiceName

class Client (models.Model):
    ClientName = models.CharField(max_length=100, verbose_name='Имя')
    ClientSurname = models.CharField(max_length=100, verbose_name='Фамилия')
    ClientPatronymic = models.CharField(max_length=100, verbose_name='Отчество')
    ClientPhone = models.CharField(max_length=20, verbose_name='Телефон')
    ClientEmail = models.EmailField(max_length=50, verbose_name='E-mail')
    User=models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    class Meta:
        verbose_name='Клиент'
        verbose_name_plural='Клиенты'
    def __str__(self):
        return '%s %s %s'%(self.ClientSurname,self.ClientName, self.ClientPatronymic)

class PaymentMethod(models.Model):
    type_choices=(('Карта','Карта'), ('Электронный кошелёк','Электронный кошелёк'),('Наличные','Наличные'))
    PaymentType=models.CharField(max_length=50, verbose_name='Тип оплаты', choices=type_choices)
    PaymentName=models.CharField(max_length=100, verbose_name='Наименование оплаты')
    class Meta:
        verbose_name = 'Способ оплаты'
        verbose_name_plural = 'Способы оплаты'
    def __str__(self):
        return self.PaymentName

from datetime import date
from django.conf import settings
from django.db.models import Sum
from django.utils import timezone
class Order(models.Model):
    Client=models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Заказчик')
    OrderDate=models.DateField(default=timezone.now(),verbose_name='Дата заказа')
    OrderRequirement=models.TextField(verbose_name='Требования')
    status_choices=(('Создан','Создан'), ('Обрабатывается','Обрабатывается'), ('Выполнен','Выполнен'))
    OrderStatus=models.CharField(max_length=50, verbose_name='Статус заказа',choices=status_choices, default='Создан', blank=True, null=True)
    Employee=models.ForeignKey(Employee,on_delete=models.CASCADE, verbose_name='Ответственный сотрудник', blank=True, null=True)
    ITService=models.ManyToManyField(ITService, verbose_name='Выбранные услуги')
    OrderPrice=models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True, verbose_name='Сумма заказа', validators=[MinValueValidator(0.01)])
    PaymentMethod=models.ForeignKey(PaymentMethod, on_delete=models.CASCADE,  verbose_name='Способ оплаты')
    class Meta:
        verbose_name='Заказ'
        verbose_name_plural='Заказы'
    def __str__(self):
        return '%s %s '%('Заказ №',self.id)

class Contract(models.Model):
    ContractNumber=models.IntegerField(verbose_name='Номер договора')
    ContractDate=models.DateField(verbose_name='Дата заключения договора')
    ContractEndDate=models.DateField(verbose_name='Дата окончания договора')
    Order=models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заказ')
    class Meta:
        verbose_name='Договор'
        verbose_name_plural='Договоры'
    def __str__(self):
        return '%s %s '%('Договор №',self.ContractNumber)