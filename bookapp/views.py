from django.shortcuts import render
from bookapp.models import User_info,flight_search,Booking,payment

# Create your views here.
def index(request):
    return render(request,'bookapp/index.html')
def flight_view(request):
    mydata=flight_search.objects.filter(source="Lucknow").values();
    return render(request,'bookapp/flight.html',{'flight_search':mydata})
def USER_REGISTRATION(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        contact=request.POST['contact']
        city=request.POST['city']
        zipcode=request.POST['zipcode']
        state=request.POST['state']
        country=request.POST['country']
        password=request.POST['password']
        gender=request.POST['gender']
        
        new_user=User_info(faname=fname,lname=lname,contact=contact,city=city,zipcode=zipcode,state=state,country=country,password=password,gender=gender)
        new_user.save();
    return render(request,'bookapp/UserRegsitraion.html',{})

def LOGIN_USER(request):
    return render(request,'bookapp/login.html')
def BOOKING(request):
    if request.method=='POST':
        user_id=request.POST['userid']
        route_id=request.POST['routeid']
        class_type=request.POST['class']
        date=request.POST['date']

        new_booking=Booking(user_id=user_id,route_id=route_id,class_type=class_type,date=date)
        new_booking.save()
    return render(request,'bookapp/bookingform.html')    
def PAYMENT(request):
    if request.method=='POST':
        user_id=request.POST['userid']
        amount =request.POST['amount']
        date=request.POST['date']

        new_payment=payment(user_id=user_id,amount=amount,date=date)
        new_payment.save()
       
    return render(request,'bookapp/payment.html')
def TICKET(request):
    return render(request,'bookapp/ticket.html')        