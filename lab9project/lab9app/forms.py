from django import forms
from .models import Products

class ProductForm(forms.Form):
    CATEGORY_CHOICES = [
        ('GENERAL_MERCHANDISE', 'General Merchandise'),
        ('FOOD_BEVERAGE', 'Food & Beverage'),
    ]

    proname = forms.CharField(label="", max_length=200, widget=forms.TextInput())
    brand = forms.CharField(label="", max_length=200, required=False, widget=forms.TextInput())
    cost = forms.DecimalField(label="", max_digits=10, decimal_places=2, required=False, widget=forms.NumberInput())
    price = forms.DecimalField(label="", max_digits=10, decimal_places=2, widget=forms.NumberInput())
    prodescription = forms.CharField(
        label="", widget=forms.Textarea(attrs={"rows": 3}), required=False
    )
    category = forms.ChoiceField(
        label="", choices=CATEGORY_CHOICES, widget=forms.Select(attrs={"onchange": "toggleFields()"})
    )
    image = forms.CharField(label="", max_length=500, required=False, widget=forms.TextInput())
    quantity_available = forms.IntegerField(label="", required=False, widget=forms.NumberInput())

    # Additional fields
    color = forms.CharField(label="", max_length=20, required=False, widget=forms.TextInput())
    sell_by = forms.DateField(label="", widget=forms.DateInput(attrs={"type": "date"}), required=False)

    def clean(self):
        cleaned_data = super().clean()
        category = cleaned_data.get("category")

        if category == "GENERAL_MERCHANDISE" and not cleaned_data.get("color"):
            raise forms.ValidationError("Color is required for General Merchandise.")

        if category == "FOOD_BEVERAGE" and not cleaned_data.get("sell_by"):
            raise forms.ValidationError("Sell By date is required for Food & Beverage.")

        return cleaned_data

#Form that handling the user input of user name and password when user sign in
class SignInForm(forms.Form):
    email = forms.EmailField(
        label="Email Address",
        max_length=100,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'})
    )
    password = forms.CharField(
        label="Password", 
        max_length=50, 
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password'})
    )


#Form that handle user signup
class SignUpForm(forms.Form):
    user_type_choices = [
        ('customer', 'Customer'),
        ('admin', 'Admin'),
    ]

    userType = forms.ChoiceField(choices=user_type_choices, widget=forms.RadioSelect, required=True)
    User_Name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    Password = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    Email_Address = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Email Address'}))
    Phone_Number = forms.CharField(max_length=15, required=False, widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}))
    
    # Customer-specific fields
    Bank_Account = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'placeholder': 'Bank Account'}))
    Home_Address = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'placeholder': 'Home Address'}))