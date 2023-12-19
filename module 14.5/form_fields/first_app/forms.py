import datetime
from django import forms

class contactForm(forms.Form):

    # Simple CharField
    name = forms.CharField(label='Name')

    # CharField with Textarea widget (default rows)
    message = forms.CharField(widget=forms.Textarea, label='About')

    # CharField with Textarea widget and custom attributes (e.g., 3 rows)
    additional_info = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 2}),
        label='Additional Information'
    )

    # EmailField
    email = forms.EmailField(label='Email')

    # DateField
    BIRTH_YEAR_CHOICES = ['1997','1998','1999']
    
    birth_date = forms.DateField(
        label='Date of birth',
        initial=datetime.date.today,
        widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES)
    )



    # New DecimalField
    salary = forms.DecimalField(
        max_digits=10,  # Maximum number of digits, including decimal places
        decimal_places=2,  # Number of decimal places
        label='Your Salary'
    )

    # New ChoiceField with RadioSelect widget
    gender_choices = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    gender = forms.ChoiceField(
        choices=gender_choices,
        widget=forms.RadioSelect,
        label='Gender'
    )


    # New MultipleChoiceField
    fruit_choices = [
        ('mango', 'Mango'),
        ('orange', 'Orange'),
        ('banana', 'Banana'),
        
    ]
    
    favorite_fruits = forms.MultipleChoiceField(
        choices=fruit_choices,
        label='Favorite Fruits'
    )
    
    # New MultipleChoiceField with CheckboxSelectMultiple widget
    color_choices = [
        ('red', 'Red'),
        ('green', 'Green'),
        ('blue', 'Blue'),
    ]
    
    favorite_colors = forms.MultipleChoiceField(
        choices=color_choices,
        widget=forms.CheckboxSelectMultiple,
        label='Favorite Colors'
    )


    # BooleanField (Checkbox)
    subscribe_to_newsletter = forms.BooleanField(
        required=False,
        initial=True,  # Default value (checked)
        label='Subscribe'
    )
