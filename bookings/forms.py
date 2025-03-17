from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Booking, Table

class CustomUserCreationForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15, required=True)
    role = forms.ChoiceField(choices=CustomUser.ROLE_CHOICES)

    class Meta:
        model = CustomUser
        fields = ["username", "email", "phone_number", "role", "password1", "password2"]

class BookingForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))

    class Meta:
        model = Booking
        fields = ["table", "date", "time", "guests"]

    def clean(self):
        cleaned_data = super().clean()
        table = cleaned_data.get("table")
        date = cleaned_data.get("date")
        time = cleaned_data.get("time")

        # Check if the selected table is already booked for the same date & time
        if Booking.objects.filter(table=table, date=date, time=time).exists():
            raise forms.ValidationError("This table is already booked for the selected date and time.")
        return cleaned_data
