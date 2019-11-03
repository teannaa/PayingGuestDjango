from django import forms


GENDER_CHOICES = (
   ('0', 'Male'),
   ('1', 'Female')
)

WIFI_CHOICES = (
   ('0', 'Not Available'),
   ('1', 'Available')
)

AC_CHOICES = (
   ('0', 'Non AC'),
   ('1', 'AC')
)

BED_CHOICES = (
   ('1', '1BHK'),
   ('2', '2BHK'),
   ('3','3BHK'),
   ('6', '6BHK')
)


class SignupForm(forms.Form):
    firstname=forms.CharField(widget=forms.TextInput())
    lastname =forms.CharField(widget=forms.TextInput())
    email=forms.EmailField(widget=forms.EmailInput())
    password1=forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())

class PayingGuestDetailsForm(forms.Form):
    city=forms.CharField(label='City',widget=forms.TextInput())
    state=forms.CharField(label='State',widget=forms.TextInput())
    nearestLandmark = forms.CharField(label='Nearest Landmark',widget=forms.TextInput())
    no_of_beds = forms.CharField(label='Number of Beds',widget=forms.RadioSelect(choices=BED_CHOICES))
    price = forms.CharField(label='Price(per bed)',widget=forms.TextInput())
    gst = forms.CharField(label='GST',widget=forms.TextInput())
    wifi_no_wifi = forms.CharField(label='Wifi Access',widget=forms.RadioSelect(choices=WIFI_CHOICES))
    ac_no_ac = forms.CharField(label='AC/Non-AC',widget=forms.RadioSelect(choices=AC_CHOICES))
    male_or_female = forms.CharField(label='Male/Female',widget=forms.RadioSelect(choices=GENDER_CHOICES))
    publishedDate = forms.DateField(label='Date Published', widget=forms.SelectDateWidget)

class SearchForm(forms.Form):
    city = forms.CharField(label='City', widget=forms.TextInput())
    state = forms.CharField(label='State', widget=forms.TextInput())
    male_or_female = forms.CharField(label='Male/Female', widget=forms.RadioSelect(choices=GENDER_CHOICES))
