from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from .models import GuestHouses, RoomCategories, GuestCategories, RoomRates,Rooms,Reservation
from django.contrib.auth import login, logout, authenticate
from django.views.generic import CreateView
from .form import *
from .models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

def homepage(request):
    guesthouses = GuestHouses.objects.all()
    room_categories = RoomCategories.objects.none()
    guest_categories = GuestCategories.objects.none()
    room_rates = []

    if request.method == "POST":
        guesthouse_id = request.POST.get("guesthouse")
        room_category_id = request.POST.get("room_category")
        guest_category_id = request.POST.get("guest_category")

        if guesthouse_id:
            room_categories = RoomCategories.objects.filter(
                guesthouse_name_id=guesthouse_id
            )
            if room_category_id:
                guest_categories = GuestCategories.objects.filter(
                    room_category_id=room_category_id
                )
                if guest_category_id:
                    room_rates = RoomRates.objects.filter(
                        room_category_id=room_category_id,
                        guest_category_id=guest_category_id,
                    )

    return render(
        request,
        "index.html",
        {
            "guesthouses": guesthouses,
            "room_categories": room_categories,
            "guest_categories": guest_categories,
            "room_rates": room_rates,
        },
    )


def get_room_categories(request, guesthouse_id):
    room_categories = RoomCategories.objects.filter(
        guesthouse_name_id=guesthouse_id
    ).values("id", "room_cat")
    return JsonResponse({"options": list(room_categories)})


def get_guest_categories(request, room_category_id):
    guest_categories = GuestCategories.objects.filter(
        room_category_id=room_category_id
    ).values("id", "guestcategory_name")
    return JsonResponse({"options": list(guest_categories)})



class customer_signup(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = "../templates/customer/customer_signup.html"

    def form_valid(self, form):
        messages.success(self.request, "Account created successfully!!")
        user = form.save()
        return redirect("customer_login")


class employee_signup(CreateView):
    model = User
    form_class = EmployeeSignUpForm
    template_name = "../templates/employee/employee_signup.html"

    def form_valid(self, form):
        user = form.save()
        messages.success(self.request, "Account created successfully!!")
        return redirect("employee_login")


def customer_login(request):
    if request.user.is_authenticated:
        return redirect("/")
    elif request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_employee:
                    messages.error(
                        request, "You do not have permission to access this page."
                    )
                    return redirect("/customer_login")
                else:
                    login(request, user)
                    return redirect("/")
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")
    return render(
        request, "customer/customer_login.html", context={"form": AuthenticationForm()}
    )


def employee_login(request):
    if request.user.is_authenticated:
        return redirect("/")
    elif request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_customer:
                    messages.error(
                        request, "You do not have permission to access this page."
                    )
                    return redirect("employee_login")
                else:
                    login(request, user)
                    return redirect("/")
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")
    return render(
        request, "employee/employee_login.html", context={"form": AuthenticationForm()}
    )


def logout_view(request):
    logout(request)
    return redirect("/")


@login_required
def customer_dash(request):
    if request.user.is_customer == False:
        return HttpResponse('Access Denied')
    return render(request, "customer/customer_dash.html")

@login_required(login_url='/')
def employee_dash(request):
    if not request.user.is_employee:
        return redirect("employee_login")
    return render(request, "employee/employee_dash.html")


def guesthouseshw(request):
    employees = GuestHouses.objects.all()
    return render(request, "employee/guesthouseshw.html", {'employees': employees})


@login_required
def request(request):
    if request.user.is_customer == False:
        messages.error(request, "Your are not eligible for login here .Please create or login as a customer to access this page ")
        return redirect("customer_login")
    if request.method == "POST":
        form = RequestForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Your Booking Request Has beeb submitted Successfully")
                return redirect('/')
            except:
                pass
    else:
        form = RequestForm()
    return render(request,'customer/request.html',{'form':form})

def approval(request):
    if request.method == "POST":
        form = ApprovalForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Data inserted successfully")
            except:
                pass
    else:
        form = ApprovalForm()
    return render(request,'employee/approval.html',{'form':form})
def roomrates(request):
    stu1 = RateForm()
    return render(request, "employee/roomrates.html", {"form": stu1})


def create_room_rate(request):
    if request.method == 'POST':
        form = RoomRateForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = RoomRateForm()

    return render(request, 'employee/rr.html', {'form': form})

def addguesthouse(request):
    if request.method == 'POST':
        form = GuesthouseForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = GuesthouseForm()

    return render(request, 'employee/addguesthouse.html', {'form': form})

def addroomcategories(request):
    if request.method == 'POST':
        form = RoomCategoriesForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = RoomCategoriesForm()

    return render(request, 'employee/addroomcategories.html', {'form': form})

def show(request):
    employees = Request.objects.all()
    return render(request,"employee/requestshow.html",{'employees':employees})

def viewroomcategories(request):
    roomcategories = RoomCategories.objects.all()
    return render(request,"employee/viewroomcategories.html",{'roomcategories':roomcategories})

def addguestcategories(request):
    if request.method == 'POST':
        form = GuestCategoriesForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = GuestCategoriesForm()

    return render(request, 'employee/addguestcategories.html', {'form': form})
def viewguestcategories(request):
    guestcategories = GuestCategories.objects.all()
    return render(request,"employee/viewguestcategories.html",{'guestcategories':guestcategories})


def addroomrates(request):
    if request.method == 'POST':
        form =RateForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = RateForm()

    return render(request, 'employee/addroomrates.html', {'form': form})


def addbooking(request):
    if request.method == 'POST':
        form1 = CustomerForm(request.POST)
        form = BookingForm(request.POST)

        if form1.is_valid() and form.is_valid():
            customer_instance = form1.save()
            booking_instance = form.save(commit=False)
            booking_instance.customer = customer_instance
            booking_instance.save()
            return redirect('booking_success')  # Replace 'booking_success' with your success URL

    else:
        form1 = CustomerForm(initial={'employee': request.user.username})
        form = BookingForm(initial={'no_of_days': 12})

    return render(request, 'employee/addbooking.html', {'form': form, 'form1': form1})
def viewbooking(request):
    reservation = Reservation.objects.all()
    return render (request,"employee/viewbooking.html",{'reservation':reservation})


def viewrooms(request):

    rooms = Rooms.objects.all()
    return render (request,"employee/viewrooms.html",{'rooms':rooms})
def addrooms(request):
    if request.method == 'POST':
        form =RoomsForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = RoomsForm()

    return render(request, 'employee/addrooms.html', {'form': form})

def update(request, id):
    employee = Request.objects.get(id=id)
    form = RequestForm(request.POST, instance = employee)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html', {'employee': employee})
def viewroomrates(request):
    roomrates = RoomRates.objects.all()
    return render (request,"employee/viewroomrates.html",{'roomrates':roomrates})
def booking_procedure(request):
    return render(request, "booking_procedure.html")
def images(request):
    return render(request, "images.html")
def contact_us(request):
    return render(request, "contact_us.html")
def committee(request):
    return render(request, "committee.html")
def imp_info(request):
    return render(request, "imp_info.html")
