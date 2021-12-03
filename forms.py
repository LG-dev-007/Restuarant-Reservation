from django import forms
from django.forms.models import ModelForm
from django.forms.widgets import DateInput

from main.models import UserReservation

MAX_CAPACITY = [tuple([x,x]) for x in range(1,20)]

class DateInput(forms.DateInput):
    input_type= 'date'

class TimeInput(forms.TimeInput):
    input_type='time'

class RegisterUser(forms.Form):     
    fname = forms.CharField(label="First Name", max_length=200)
    lname = forms.CharField(label="Last Number",max_length=200)
    username = forms.CharField(label="username",max_length=200)
    email = forms.CharField(label="Email",max_length=200)
    password1 = forms.CharField(label="password1", max_length=200)
    password2 = forms.CharField(label="password2", max_length=200)
    
    # mail_add = forms.CharField(label="Mailing address", max_length=200)
    # bill_add = forms.CharField(label="Billing address", max_length=200)
    
class ReserveTable(ModelForm):     #forms.Form
    class Meta:
        model = UserReservation
        fields = ['name', 'phone', 'email']
    # name= forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Name"}), max_length=200)
    # phone= forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Phone number"}), max_length=200)
    # email= forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Email"}), max_length=200)
    select_tables=forms.IntegerField(label="Enter your party:", widget=forms.Select(choices=MAX_CAPACITY))
    select_date=forms.DateField(label="Select a date", widget=DateInput)
    select_time=forms.TimeField(label="Select a time", widget=TimeInput)

    # def save(self):
    #     cleaned_data = self.cleaned_data

class PaymentForm(forms.Form):
    #name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Full name"}), max_length=200)
    fName = forms.CharField(label="First Name", widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "First Name"}), max_length=200)
    lName = forms.CharField(label="Last Name", widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Last Name"}), max_length=200)
    email = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Email Address"}), max_length = 200)
    Address = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Address"}), max_length = 200)
    Address2 = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Address 2"}), max_length = 200, required = False, label="Address 2")
    city = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "City"}), max_length = 200)
    state = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "State"}), max_length = 200)
    zipcode = forms.CharField(label="Zip", widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Zip Code"}), max_length=200)
    cardName = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Full Name On Card"}), max_length=200, label="Name On Card")
    card = forms.CharField(label="Card Number", widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "xxxx-xxxx-xxxx-xxxx"}), max_length = 200)
    expiration = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "MM/YY"}), max_length=200, label="Expiration")
    cvv = forms.CharField(label="CVV", widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "CVV"}), max_length = 200)
    

class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=200)
    password = forms.CharField(label="Password", max_length=200)

