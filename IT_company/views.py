from django.shortcuts import render, get_object_or_404
from .models import Branches, Department, Employee, ITService, ServiceType, PaymentMethod, Equipment, Order, Client, Stock, Provider, Post, Contract
from django.core.paginator import Paginator, PageNotAnInteger,EmptyPage
from .forms import EmployeeForm, BranchForm, DepartmentForm, ITServiceForm, FilterForm, PaymentMethodForm, EquipmentForm, ClientForm, OrderForm, EmpOrderForm, StockForm, ProviderForm, PostForm, OrderSearch, ServiceTypeForm, ContractForm, ContractSearchForm, EmpClientForm
from django.shortcuts import redirect

def home(request):
    return render(request, 'blog/home.html')

from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})

from django.contrib.auth.decorators import login_required

from .forms import LoginForm, UserRegistrationForm

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'registration/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'user_form': user_form})

def branches_list(request):
    queryset_list = Branches.objects.all().order_by("id")
    paginator = Paginator(queryset_list, 3)  # posts per page
    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    context = {
        "object_list": queryset,
    }
    return render(request, 'blog/branches_list.html', context)

def branch_detail(request, pk):
    branch=get_object_or_404(Branches, pk=pk)
    return render(request, 'blog/branch_detail.html', {'branch':branch})

def branch_edit(request, pk):
    branch = get_object_or_404(Branches, pk=pk)
    if request.method == "POST":
        form = BranchForm(request.POST, instance=branch)
        if form.is_valid():
            branch = form.save(commit=False)
            branch.save()
            return redirect('branch_detail', pk=branch.pk)
    else:
        form = BranchForm(instance=branch)
    return render(request, 'blog/branch_edit.html', {'form': form})

def branch_new(request):
    if request.method == "POST":
        form = BranchForm(request.POST)
        if form.is_valid():
            branch = form.save(commit=False)
            branch.save()
            return redirect('branch_detail', pk=branch.pk)
    else:
        form = BranchForm()
    return render(request, 'blog/branch_edit.html', {'form': form})

def branch_remove(request, pk):
    branch=get_object_or_404(Branches, pk=pk)
    branch.delete()
    return  redirect('branch_list')

def department_list(request):
    queryset_list = Department.objects.all().order_by("id")
    paginator = Paginator(queryset_list, 3)  # posts per page
    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    context = {
        "object_list": queryset,
    }
    return render(request, 'blog/department_list.html', context)

def department_detail(request, pk):
    department=get_object_or_404(Department, pk=pk)
    employees=Employee.objects.filter(Department=pk)
    return render(request, 'blog/department_detail.html', {'department':department, 'employees':employees})

def department_remove(request, pk):
    department=get_object_or_404(Department, pk=pk)
    department.delete()
    return  redirect('department_list')

def  department_edit(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == "POST":
        form = DepartmentForm(request.POST, instance= department)
        if form.is_valid():
            department = form.save(commit=False)
            department.save()
            return redirect('department_detail', pk= department.pk)
    else:
        form = DepartmentForm(instance= department)
    return render(request, 'blog/department_edit.html', {'form': form})

def department_new(request):
    if request.method == "POST":
        form = DepartmentForm(request.POST)
        if form.is_valid():
            department = form.save(commit=False)
            department.save()
            return redirect('department_detail', pk=department.pk)
    else:
        form = DepartmentForm()
    return render(request, 'blog/department_edit.html', {'form': form})


def stock_list(request):
    queryset_list = Stock.objects.all().order_by("id")
    paginator = Paginator(queryset_list, 3)  # posts per page
    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    context = {
        "object_list": queryset,
    }
    return render(request, 'blog/stock_list.html', context)

def stock_detail(request, pk):
    stock=get_object_or_404(Stock, pk=pk)
    return render(request, 'blog/stock_detail.html', {'stock': stock})

def stock_edit(request, pk):
    stock = get_object_or_404(Stock, pk=pk)
    if request.method == "POST":
        form = StockForm(request.POST, instance=stock)
        if form.is_valid():
            stock = form.save(commit=False)
            stock.save()
            return redirect('stock_detail', pk=stock.pk)
    else:
        form = StockForm(instance=stock)
    return render(request, 'blog/stock_edit.html', {'form': form})

def stock_new(request):
    if request.method == "POST":
        form = StockForm(request.POST)
        if form.is_valid():
            stock = form.save(commit=False)
            stock.save()
            return redirect('stock_detail', pk=stock.pk)
    else:
        form = StockForm()
    return render(request, 'blog/stock_edit.html', {'form': form})

def stock_remove(request, pk):
    stock=get_object_or_404(Stock, pk=pk)
    stock.delete()
    return  redirect('stock_list')

def provider_list(request):
    queryset_list = Provider.objects.all().order_by("id")
    paginator = Paginator(queryset_list, 3)  # posts per page
    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    context = {
        "object_list": queryset,
    }
    return render(request, 'blog/provider_list.html', context)

def provider_detail(request, pk):
    provider=get_object_or_404(Provider, pk=pk)
    return render(request, 'blog/provider_detail.html', {'provider':provider})

def provider_edit(request, pk):
    provider = get_object_or_404(Provider, pk=pk)
    if request.method == "POST":
        form = ProviderForm(request.POST, instance=provider)
        if form.is_valid():
            provider = form.save(commit=False)
            provider.save()
            return redirect('provider_detail', pk=provider.pk)
    else:
        form = ProviderForm(instance=provider)
    return render(request, 'blog/provider_edit.html', {'form': form})

def provider_new(request):
    if request.method == "POST":
        form = ProviderForm(request.POST)
        if form.is_valid():
            provider = form.save(commit=False)
            provider.save()
            return redirect('provider_detail', pk=provider.pk)
    else:
        form = ProviderForm()
    return render(request, 'blog/provider_edit.html', {'form': form})

def provider_remove(request, pk):
    provider=get_object_or_404(Provider, pk=pk)
    provider.delete()
    return  redirect('provider_list')

from django.db.models import Q
from django.views.generic import TemplateView, ListView

class client_search(ListView):
    model = Client
    template_name = 'blog/client_search.html'
    def get_queryset(self):  # новый
        queryset=Client.objects.all()
        q = self.request.GET.get('q')
        if q:
            return  queryset.filter(
            Q(ClientSurname__icontains=q)| Q(ClientName__icontains=q)
        )
        return queryset

class employee_search(ListView):
    model = Employee
    template_name = 'blog/employee_search.html'
    def get_queryset(self):  # новый
        queryset=Employee.objects.all()
        q = self.request.GET.get('q')
        if q:
            return  queryset.filter(
            Q(EmpSurname__icontains=q)| Q(EmpName__icontains=q)
        )
        return queryset

def employeelist(request):
    is_MainManager = request.user.groups.filter(name='MainManager').exists()
    queryset_list = Employee.objects.all().order_by("id")
    paginator = Paginator(queryset_list, 3)  # posts per page
    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    context = {
        "object_list": queryset,
        "is_MainManager": is_MainManager,
    }
    return render(request, 'blog/employeelist.html', context)

def employee_detail(request, pk):
    employee=get_object_or_404(Employee, pk=pk)
    return render(request, 'blog/employee_detail.html', {'employee':employee})

def employee_edit(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.save()
            return redirect('employee_detail', pk=employee.pk)
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'blog/employee_edit.html', {'form': form})

def employee_new(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.save()
            return redirect('employee_detail', pk=employee.pk)
    else:
        form = EmployeeForm()
    return render(request, 'blog/employee_edit.html', {'form': form})

def employee_remove(request, pk):
    employee=get_object_or_404(Employee, pk=pk)
    employee.delete()
    return  redirect('employee_list')

def itservice_detail(request, pk):
    itservice=get_object_or_404(ITService, pk=pk)
    equips=itservice.Equipments.all()
    return render(request, 'blog/itservice_detail.html', {'itservice': itservice, 'equips':equips})

def itservice_edit(request, pk):
    itservice = get_object_or_404(ITService, pk=pk)
    if request.method == "POST":
        form = ITServiceForm(request.POST, instance=itservice)
        if form.is_valid():
            itservice = form.save()
            itservice.save()
            return redirect('itservice_detail', pk=itservice.pk)
    else:
        form = ITServiceForm(instance=itservice)
    return render(request, 'blog/itservice_edit.html', {'form': form})

def itservice_new(request):
    if request.method == "POST":
        form = ITServiceForm(request.POST)
        if form.is_valid():
            itservice = form.save()
            itservice.save()
            return redirect('itservice_detail', pk=itservice.pk)
    else:
        form = ITServiceForm()
    return render(request, 'blog/itservice_edit.html', {'form': form})

def itservice_remove(request, pk):
    itservice=get_object_or_404(ITService, pk=pk)
    itservice.delete()
    return  redirect('productlist')

def servicetype_list(request):
    queryset_list = ServiceType.objects.all().order_by("id")
    context = {
        "object_list": queryset_list,
    }
    return render(request, 'blog/servicetype_list.html', context)
from django.utils.text import slugify
def servicetype_new(request):
    if request.method == "POST":
        form = ServiceTypeForm(request.POST, request.FILES,)
        if form.is_valid():
            servicetype = form.save(commit=False)
            servicetype.slug=slugify(servicetype.TypeName, allow_unicode=True)
            servicetype.save()
            return redirect('servicetype_detail', pk=servicetype.pk)
    else:
        form = ServiceTypeForm()
    return render(request, 'blog/servicetype_edit.html', {'form': form})

def servicetype_detail(request, pk):
    servicetype=get_object_or_404(ServiceType, pk=pk)
    return render(request, 'blog/servicetype_detail.html', {'servicetype': servicetype})

def servicetype_edit(request, pk):
    servicetype = get_object_or_404(ServiceType, pk=pk)
    if request.method == "POST":
        form = ServiceTypeForm(request.POST, request.FILES, instance=servicetype)
        if form.is_valid():
            servicetype = form.save(commit=False)
            servicetype.save()
            return redirect('servicetype_detail', pk=servicetype.pk)
    else:
        form = ServiceTypeForm(instance=servicetype)
    return render(request, 'blog/servicetype_edit.html', {'form': form})

def servicetype_remove(request, pk):
    servicetype=get_object_or_404(ServiceType, pk=pk)
    servicetype.delete()
    return redirect('product_list')

def equipment_detail(request, pk):
    equipment=get_object_or_404(Equipment, pk=pk)
    return render(request, 'blog/equipment_detail.html', {'equipment':equipment})

def equipment_edit(request, pk):
    equipment = get_object_or_404(Equipment, pk=pk)
    if request.method == "POST":
        form = EquipmentForm(request.POST, instance=equipment)
        if form.is_valid():
            equipment = form.save(commit=False)
            equipment.save()
            return redirect('equipment_detail', pk=equipment.pk)
    else:
        form = EquipmentForm(instance=equipment)
    return render(request, 'blog/equipment_edit.html', {'form': form})

def equipment_list(request):
    queryset_list = Equipment.objects.all().order_by("id")
    paginator = Paginator(queryset_list, 3)  # posts per page
    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    context = {
        "object_list": queryset,
    }
    return render(request, 'blog/equipment_list.html', context)

def equipment_new(request):
    if request.method == "POST":
        form = EquipmentForm(request.POST)
        if form.is_valid():
            equipment = form.save(commit=False)
            equipment.save()
            return redirect('equipment_detail', pk=equipment.pk)
    else:
        form = EquipmentForm()
    return render(request, 'blog/equipment_edit.html', {'form': form})

def equipment_remove(request, pk):
    equipment=get_object_or_404(Equipment, pk=pk)
    equipment.delete()
    return redirect('equipment_list')

def itservice_list(request, category_slug=None):
    form=FilterForm(request.GET)
    category = None
    categories = ServiceType.objects.all()
    products = ITService.objects.filter(ServiceAvailable=True)
    if form.is_valid():
        if form.cleaned_data["min_price"]:
            products = products.filter(ServicePrice__gte=form.cleaned_data["min_price"])
        if form.cleaned_data["max_price"]:
            products = products.filter(ServicePrice__lte=form.cleaned_data["max_price"])
    if category_slug:
        category = get_object_or_404(ServiceType, slug=category_slug)
        products = products.filter(ServiceType=category)
        if form.is_valid():
            if form.cleaned_data["min_price"]:
                products = products.filter(ServicePrice__gte=form.cleaned_data["min_price"])
            if form.cleaned_data["max_price"]:
                products = products.filter(ServicePrice__lte=form.cleaned_data["max_price"])
    return render(request,
                  'blog/productlist.html',
                  {'category': category,
                   'categories': categories,
                   'products': products,
                   'form':form})

from django.shortcuts import HttpResponseRedirect
from django.utils import timezone
def new_person(request):
    if request.method == "POST":
        client_form = ClientForm(request.POST)
        order_form = OrderForm(request.POST)
        if order_form.is_valid() and client_form.is_valid():
            client_f = client_form.save(commit=False)
            order_f = order_form.save(commit=False)
            client_f.save()
            order_f.Client = client_f
            order_f.save()
            client_form.save_m2m()
            order_form.save_m2m()
            order_f.OrderPrice = order_f.ITService.aggregate(Sum('ServicePrice'))['ServicePrice__sum']
            order_f.save()
            return HttpResponseRedirect('/order_list')
    else:
        client_form = ClientForm()
        order_form = OrderForm()
    context = {
        'client_form': client_form,
        'order_form': order_form,
    }
    return render(request, 'blog/ClientOrderForm.html', context)

def order_list(request):
    queryset_list = Order.objects.all().order_by("id")
    form = OrderSearch(request.GET)
    if form.is_valid():
        if form.cleaned_data["OrderStatus"]:
            queryset_list = queryset_list.filter(OrderStatus=form.cleaned_data["OrderStatus"])
    context = {
        "object_list": queryset_list, "form":form
    }
    return render(request, 'blog/order_list.html', context)

def client_list(request):
    queryset_list = Client.objects.all().order_by("ClientSurname")
    context = {
        "object_list": queryset_list,
    }
    return render(request, 'blog/client_list.html', context)

def order_detail(request, pk):
    order=get_object_or_404(Order, pk=pk)
    services = order.ITService.all()
    return render(request, 'blog/order_detail.html', {'order':order, 'services':services})

def order_edit(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == "POST":
        form = EmpOrderForm(request.POST, instance=order)
        if form.is_valid():
            order = form.save()
            order.save()
            order.OrderPrice = order.ITService.aggregate(Sum('ServicePrice'))['ServicePrice__sum']
            order.save()
            return redirect('order_detail', pk=order.pk)
    else:
        form = EmpOrderForm(instance=order)
    return render(request, 'blog/order_edit.html', {'form': form})

def clientorder_list(request):
    client = get_object_or_404(Client, User=request.user)
    orders = Order.objects.filter(Client=client)
    return render(request, 'blog/client_detail.html', {'client': client, 'orders': orders})

def client_detail(request, pk):
    client=get_object_or_404(Client, pk=pk)
    orders=Order.objects.filter(Client=pk)
    return render(request, 'blog/client_detail.html', {'client':client, 'orders':orders})

def client_new(request):
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            client.User=request.user
            client.save()
            return redirect('client_detail', pk=client.pk)
    else:
        form = ClientForm()
    return render(request, 'blog/client_edit.html', {'form': form})

def empclient_new(request):
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            client.save()
            return redirect('client_detail', pk=client.pk)
    else:
        form = ClientForm()
    return render(request, 'blog/client_edit.html', {'form': form})
from django.db.models import Sum
from datetime import date
def order_new(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False) #или пользователь, или м:м
            order.Client=Client.objects.get(User=request.user)
            order.save()
            form.save_m2m()
            order.OrderPrice=order.ITService.aggregate(Sum('ServicePrice'))['ServicePrice__sum']
            order.save()
            return redirect('order_detail', pk=order.pk)
    else:
        form = OrderForm()
    return render(request, 'blog/order_edit.html', {'form': form})

def order_remove(request, pk):
    order=get_object_or_404(Order, pk=pk)
    order.delete()
    return  redirect('order_list')

def client_edit(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == "POST":
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            client = form.save(commit=False)
            client.save()
            return redirect('client_detail', pk=client.pk)
    else:
        form = ClientForm(instance=client)
    return render(request, 'blog/client_edit.html', {'form': form})

def empclient_edit(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == "POST":
        form = EmpClientForm(request.POST, instance=client)
        if form.is_valid():
            client = form.save(commit=False)
            client.save()
            return redirect('client_detail', pk=client.pk)
    else:
        form = EmpClientForm(instance=client)
    return render(request, 'blog/client_edit.html', {'form': form})

def client_remove(request, pk):
    client=get_object_or_404(Client, pk=pk)
    client.delete()
    return  redirect('client_list')

def emporder_new(request):
    if request.method == "POST":
        form = EmpOrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            order.save()
            order.OrderPrice = order.ITService.aggregate(Sum('ServicePrice'))['ServicePrice__sum']
            order.save()
            return redirect('order_detail', pk=order.pk)
    else:
        form = EmpOrderForm()
    return render(request, 'blog/order_edit.html', {'form': form})

def post_list(request):
    queryset_list = Post.objects.all().order_by("id")
    paginator = Paginator(queryset_list, 10)  # posts per page
    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    context = {
        "object_list": queryset,
    }
    return render(request, 'blog/post_list.html', context)

def post_detail(request, pk):
    post=get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_remove(request, pk):
    post=get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')

def paymentmethod_list(request):
    queryset_list = PaymentMethod.objects.all().order_by("id")
    context = {
        "object_list": queryset_list,
    }
    return render(request, 'blog/paymentmethod_list.html', context)

def paymentmethod_detail(request, pk):
    paymentmethod=get_object_or_404(PaymentMethod, pk=pk)
    return render(request, 'blog/paymentmethod_detail.html', {'paymentmethod': paymentmethod})

def paymentmethod_remove(request, pk):
    paymentmethod=get_object_or_404(PaymentMethod, pk=pk)
    paymentmethod.delete()
    return redirect('paymentmethod_list')

def paymentmethod_edit(request, pk):
    paymentmethod = get_object_or_404(PaymentMethod, pk=pk)
    if request.method == "POST":
        form = PaymentMethodForm(request.POST, instance=paymentmethod)
        if form.is_valid():
            paymentmethod = form.save(commit=False)
            paymentmethod.save()
            return redirect('paymentmethod_detail', pk=paymentmethod.pk)
    else:
        form = PaymentMethodForm(instance=paymentmethod)
    return render(request, 'blog/paymentmethod_edit.html', {'form': form})

def paymentmethod_new(request):
    if request.method == "POST":
        form = PaymentMethodForm(request.POST)
        if form.is_valid():
            paymentmethod = form.save()
            paymentmethod.save()
            return redirect('paymentmethod_detail', pk=paymentmethod.pk)
    else:
        form = PaymentMethodForm()
    return render(request, 'blog/paymentmethod_edit.html', {'form': form})

def contract_list(request):
    form=ContractSearchForm(request.GET)
    queryset_list = Contract.objects.all().order_by("id")
    pr=0
    if form.is_valid():
        if form.cleaned_data["date1"]:
            queryset_list = queryset_list.filter(ContractDate__gte=form.cleaned_data["date1"])
        if form.cleaned_data["date2"]:
            queryset_list = queryset_list.filter(ContractEndDate__lte=form.cleaned_data["date2"])
    for c in queryset_list:
        prr = c.Order.OrderPrice
        pr = pr+prr
    context = {
        "object_list": queryset_list,"pr":pr, "form": form,
    }
    return render(request, 'blog/contract_list.html', context)

def contract_detail(request, pk):
    contract=get_object_or_404(Contract, pk=pk)

    return render(request, 'blog/contract_detail.html', {'contract': contract, })

def contract_edit(request, pk):
    contract = get_object_or_404(Contract, pk=pk)
    if request.method == "POST":
        form = ContractForm(request.POST, instance=contract)
        if form.is_valid():
            contract = form.save(commit=False)
            contract.save()
            return redirect('contract_detail', pk=contract.pk)
    else:
        form = ContractForm(instance=contract)
    return render(request, 'blog/contract_edit.html', {'form': form})

def contract_new(request):
    if request.method == "POST":
        form = ContractForm(request.POST)
        if form.is_valid():
            contract = form.save()
            contract.save()
            return redirect('contract_detail', pk=contract.pk)
    else:
        form = ContractForm()
    return render(request, 'blog/contract_edit.html', {'form': form})


def contract_remove(request, pk):
    contract=get_object_or_404(Contract, pk=pk)
    contract.delete()
    return redirect('contract_list')