from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from payingGuestApp.forms import SignupForm,LoginForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes,force_text
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.template.loader import render_to_string
from payingGuestApp.tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMultiAlternatives
from django.urls import reverse
from payingGuestApp.models import PayingGuestDetails,Location,NotificationBooth
from payingGuestApp.forms import PayingGuestDetailsForm,LoginForm,SignupForm,SearchForm


# Create your views here.
def about(request):
    return render(request, 'payingGuestApp/about.html')
def home(request):
    return render(request, 'payingGuestApp/index.html')


def sign_up(request):
    if request.method=='POST':
        print("hello")
        signup_form=SignupForm(request.POST)
        if signup_form.is_valid():
            firstname=signup_form.cleaned_data['firstname']
            lastname=signup_form.cleaned_data['lastname']
            email=signup_form.cleaned_data['email']
            password1=signup_form.cleaned_data['password1']
            password2=signup_form.cleaned_data['password2']
            username=firstname+lastname;
            if User.objects.filter(username=username).exists():
                return HttpResponse("Username already exist")
            elif password1!=password2:
                return HttpResponse("Passwords does not match");

            else:
                user=User.objects.create_user(username,email,password1)
                user.is_active = False
                user.save()
                current_site = get_current_site(request)
                mail_subject = 'Activate your blog account.'
                message = render_to_string('payingGuestApp/acc_active_account.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                })
                to_email = signup_form.cleaned_data.get('email')
                email = EmailMessage(
                    mail_subject, message, to=[to_email]
                )
                email.send()
                data = {"status": "success"}
                login(request,user)
                return HttpResponse('Please confirm your email address to complete the registration',data)
    else:
        form = SignupForm()
        return render(request, 'payingGuestApp/signUp.html', {'form': form})

def activate(request,uidb64,token):

    try:
     print(force_text(urlsafe_base64_decode(uidb64)))
     uid=force_text(urlsafe_base64_decode(uidb64))
     user=User.objects.get(pk=uid)

    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user=None
    if user is not None and account_activation_token.check_token(user,token):
        user.is_active=True
        user.save()
        return HttpResponse("Thankyou for you email confirmation")
        return HttpResponseRedirect('/payingGuestApp/logIn')
    else:
        return HttpResponse("Invalid activation")


def loginIn(request):

    if request.user.is_authenticated:
        return HttpResponse("You are aleady logged in")

    else:
        if request.method=='POST':
            login_form=LoginForm(request.POST)
            if login_form.is_valid():
                username=login_form.cleaned_data['username']
                password=login_form.cleaned_data['password']

                user=authenticate(username=username,password=password)
                if user is not None:
                    if user.is_active:
                        login(request,user)
                        return HttpResponse("Logged in successfully")

                    else:
                        return HttpResponse("Your account is not active")
                else:
                    return HttpResponse("The account does not exist")

            else:
                login_form=LoginForm()
                return render(request,'payingGuestApp/login.html',{"form":login_form})
        else:
            login_form = LoginForm()
            return render(request, 'payingGuestApp/login.html', {"form": login_form})

def searchForPg(request):

  if request.method=='POST':
      search_form=SearchForm(request.POST)
      if search_form.is_valid():
          city=search_form.cleaned_data['city']
          state=search_form.cleaned_data['state']
          male_or_female=search_form.cleaned_data['male_or_female']
          location_details = Location.objects.get(city=city,state=state)
          print(location_details)
          payingGuestDetails=PayingGuestDetails.objects.filter(location=location_details,male_or_female=male_or_female)
          print("hello")
          print(payingGuestDetails)
          context={"payingGuestDetails":payingGuestDetails}
          return render(request,'payingGuestApp/viewPg.html',context)
  else:
      form = SearchForm()
      return render(request, 'payingGuestApp/searchPg.html', {'form':form})

def insertPgDetails(request):
    if request.user.is_authenticated:
      if request.method=='POST':
        pgDetailsForm=PayingGuestDetailsForm(request.POST)
        if pgDetailsForm.is_valid():
            user=request.user
            nearestLandmark = pgDetailsForm.cleaned_data['nearestLandmark']
            no_of_beds = pgDetailsForm.cleaned_data['no_of_beds']
            price = pgDetailsForm.cleaned_data['price']
            gst = pgDetailsForm.cleaned_data['wifi_no_wifi']
            ac_no_ac = pgDetailsForm.cleaned_data['ac_no_ac']
            male_or_female = pgDetailsForm.cleaned_data['male_or_female']
            publishedDate = pgDetailsForm.cleaned_data['publishedDate']
            city=pgDetailsForm.cleaned_data['city']
            state=pgDetailsForm.cleaned_data['state']
            locationDetailsObject=Location.objects.get(city=city,state=state)
            if locationDetailsObject is None:
                locationDetailsObject=Location(city=city,state=state)
                locationDetailsObject.save()
            payingGuestDetailsObject=PayingGuestDetails(user=user,location=locationDetailsObject,nearestLandmark=nearestLandmark,
                                                     no_of_beds= no_of_beds,price=price,gst=gst,ac_no_ac=ac_no_ac,
                                                      male_or_female=male_or_female,publishedDate=publishedDate)
            payingGuestDetailsObject.save()
            return HttpResponse("Paying Guest Details added successfully")
      else:
        form=PayingGuestDetailsForm()
        return render(request,'payingGuestApp/addPg.html',{'form':form})
    else:
        return HttpResponse("To continue with the PG operations.Please Login In")

def updatePgDetails(request,pk):
    payingGuestDetails = get_object_or_404(PayingGuestDetails, pk=pk)
    if request.method=='POST':
        form = PayingGuestDetailsForm(request.POST, instance=payingGuestDetails)
        if form.is_valid():
            payingGuestDetails = form.save(commit=False)
            payingGuestDetails.save()
            return redirect('payingGuestApp/viewPg.html', pk=payingGuestDetails.pk)
    else:
        form=PayingGuestDetailsForm(instance=payingGuestDetails)
    return render(request,'payingGuestApp/editPg.html',{'form':form})

def viewPgAllDetails(request):
 payingGuestDetails=PayingGuestDetails.objects.all()
 context={"payingGuestDetails":payingGuestDetails}
 return render(request,'payingGuestApp/viewPg.html',context)



def logOut(request):
    logout(request)
    return HttpResponse("Logged out successfully")
    # Redirect to a success page.ss



