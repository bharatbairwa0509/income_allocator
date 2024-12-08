from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib import messages 
from django.urls import reverse
from ia.models import Dic
from django.contrib.auth  import authenticate,  login, logout
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import matplotlib.pyplot as plt
from io import BytesIO
import base64
def index(request):
    return render(request , 'main.html')


def about(request):
    return render(request , 'about.html')


def handleSignUp(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        # check for errorneous input
        
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        messages.success(request, " Your IA has been successfully created")
        return render(request ,'main.html')

    else:
        return HttpResponse("404 - Not found")



def handeLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['pass']
        print(loginpassword , loginusername)

        user=authenticate(username= loginusername, password = loginpassword)
        print(user)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In block")
            messages.success(request, "please give me your money expendature")
            return render(request ,'main.html')
        else:
            messages.error(request, "Invalid credentials! Please try again  2 block")
            print(loginpassword , loginusername ,"block in error ")

            return render(request ,'main.html')

    return HttpResponse("404- Not found")

def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return render(request ,'main.html')



def entertainment(request):
    return render(request , 'entertainment.html')


def rent(request):
    return render(request , 'rent.html')


def transport(request):
    return render(request , 'transport.html')


def other(request):
    return render(request , 'other.html')


def distributeI(request):

    if request.method == "POST":
        income = request.POST['income']
        Entertainment= request.POST['Entertainment']
        Transport = request.POST['Transport']
        other = request.POST['Other']
        user = request.user
        rent = request.POST['rent']


        li = Dic.objects.filter(user=user)
        print(len(li))
        if(len(li) <1):
            dis = Dic(income=income , user=user , rent = rent , transport=Transport , other =other , entertainment= Entertainment)
            dis.save()
        else:
            for item in li:
                try:
                    
        # Check if any of the attributes are None
                    if income is not None:
                        item.income += int(income)
                    if rent is not None:
                        item.rent += int(rent)
                    if Transport is not None:
                        item.transport += int(Transport)
                    if other is not None:
                        item.other += int(other)
                    if Entertainment is not None:
                        item.entertainment +=int(Entertainment)
            # Save the updated object to the database
                    item.save()
                except Exception as e:
                    print(e)


    return render(request , 'main.html')





@login_required
def expense_pie_chart_view(request):
    # Fetch data for the logged-in user
    user_data = Dic.objects.filter(user=request.user).first()
    if not user_data:
        return render(request, 'no_data.html', {'message': "No expense data found for this user."})

    # Prepare data for the pie chart
    expense_data = {
        'Rent': user_data.rent,
        'Transport': user_data.transport,
        'Other': user_data.other,
        'Entertainment': user_data.entertainment,
    }
    categories = list(expense_data.keys())
    amounts = list(expense_data.values())

    # Generate the pie chart
    plt.figure(figsize=(8, 8))
    plt.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=140)
    plt.title(f'{request.user.username}\'s Expense Distribution')

    # Save chart to a buffer
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close()

    # Encode the image to base64
    image_base64 = base64.b64encode(buffer.read()).decode('utf-8')

    return render(request, 'expense_pie_chart.html', {'graph': image_base64})



