from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from Bookings.models import Status,Tour,Customer,Booking
from .forms import LoginForm, RegistrationForm,BookTourForm
from django.db import transaction
# Create your views here.
def index(request):
	return render(request, 'booking/index.html')

#function to handle the login operations and load the Login form into the template
def login(request):
	return render(request, 'booking/login.html', {
		'form': LoginForm
	})

#User Registration function to handle the registration Operation by loading the Registration Form into the Registration Template
def register(request):
    return render(request, 'booking/registration.html', {
        'form': RegistrationForm
    })

#Function to handle the data received from the Registration Form
def registration(request):
    if request.method == 'POST':
        customerObj = Customer(name=request.POST['name'],contact=request.POST['contact'],
                               password=request.POST['password'],email=request.POST['email'],
                               address=request.POST['address'])
        customerObj.save()
    return render(request, 'booking/dashboard.html')

#User Dashboard helps to store and validate the data received from the Registration and Login Forms
def dashboard(request):
    if request.method == 'POST':
        name = request.POST['name']
        contact = request.POST['contact']
        password = request.POST['password']
        customerValidate = Customer.objects.filter(contact=contact).exists()
        if not customerValidate:
            return render(request, 'booking/login.html', {
                'form': LoginForm(initial={'contact': contact,'name' :name}, auto_id=False),
                'error_message': 'Вы не зарегестрированы'
            })
        if Customer.objects.get(contact=contact).password != password :
            return render(request, 'booking/login.html', {
                'form': LoginForm(initial={'contact': contact , 'name' :name}, auto_id=False),
                'error_message': 'У вас что-то не мэтчнулось, перепроверьте данные'
            })
        customerObj = Customer.objects.get(contact=contact)
        request.session['customerPk']=customerObj.pk
        print(request.session)
        return render(request , 'booking/dashboard.html',{'CustName': customerObj.name})


#Function to call and load the Tour Booking Form into the template
def bookTour(request):
    return render(request, 'booking/bookTour.html', {
        'form': BookTourForm
    })

#Function to handle the data received from the tour Booking Form
def bookingResult(request):
    if request.method == 'POST':
        tourList = list(Tour.objects.filter(location__iexact=request.POST['location']).values_list('name',flat=True))
        request.session['location'] = request.POST['location']
        if request.POST['amount']:
            request.session['amount']=request.POST['amount']

        if request.POST['checkInDate']:
            request.session['checkInDate'] = request.POST['checkInDate']

        if request.POST['checkOutDate']:
            request.session['checkOutDate'] = request.POST['checkOutDate']

        return render(request, 'booking/tourList.html', {'tourList': tourList})


#function that does the actual Booking by storing the data in the Database. The function is atomic with Rollback Functionality
#so that the booking can be reverted back in case of Connectivity Failure
@transaction.atomic
def bookingConfirmation(request):
    request.session['tourName']=request.POST['tourName']
    TourObj = Tour.objects.get(name=request.session['tourName'])
    customerObj = Customer.objects.get(pk=request.session['customerPk'])
    totalCount = TourObj.visitorCount + 1
    TourObj.visitorCount = totalCount
    TourObj.save()
    print(request.POST)
    try:
        if request.POST['Book']:
            bookingObj = Booking(h_id=TourObj,c_id=customerObj,amount=request.session['amount'],
                                 status=Status.objects.get(status="МЕСТ НЕТ"),checkInDate=request.session['checkInDate'],
                                 checkOutDate=request.session['checkOutDate'])
            bookingObj.save()
            return render(request, 'booking/booking_success.html')
    except :
        bookingObj = Booking(h_id=TourObj, c_id=customerObj, amount=request.session['amount'],
                             status=Status.objects.get(status="ДОСТУПНО"), checkInDate=request.session['checkInDate'],
                             checkOutDate=request.session['checkOutDate'])
        bookingObj.save()
        return render(request, 'booking/draft_saved.html')



#to check the number of visits to a particular tour
def catalog(request):
    tourList = Tour.objects.all()
    return render(request,'booking/catalog.html',{'tourList': tourList})

#function provides the data for displaying the draft Booking Functionality
def myBooking(request):
    print(request.session['customerPk'])
    bookingListObj = list(Booking.objects.filter(status=Status.objects.get(status="ДОСТУПНО"))
                          .filter(c_id=request.session['customerPk']))
    print(bookingListObj)
    if len(bookingListObj) == 0:
        return HttpResponse("???")
    return render(request, 'booking/my_booking.html',{'bookingListObj':bookingListObj})