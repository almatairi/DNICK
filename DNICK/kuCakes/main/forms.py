from django import forms
from .models import Cake

class CakeForm(forms.ModelForm):
    OCCASION_CHOICES = (
        ('Birthdays', 'Birthdays'),
        ('Anniversaries', 'Anniversaries'),
        ('Weddings', 'Weddings'),
        ('Baby showers', 'Baby showers'),
        ('Graduations', 'Graduations'),
        ('Holidays', 'Holidays'),
    )

    SERVING_SIZE_CHOICES = (
        ('5 inch (5 dessert servings)', '5 inch (5 dessert servings)'),
        ('6 inch (10 dessert servings)', '6 inch (10 dessert servings)'),
    )

    FLAVOR_CHOICES = (
        ('Chocolate', 'Chocolate'),
        ('Vanilla', 'Vanilla'),
        ('Red velvet', 'Red velvet'),
        ('Cheesecake', 'Cheesecake'),
        ('Pound', 'Pound'),
    )

    TOPPINGS_CHOICES = (
        ('Sprinkles', 'Chocolate chips'),
        ('Fruit', 'Whipped cream'),
        ('Frosting', 'Glaze'),
        ('Chocolate ganache', 'Meringue'),
        ('Nuts', 'Candy'),
        ('Chocolate shavings', 'Coconut flakes'),
        ('Marzipan', 'Rice krispies'),
        ('Edible glitter', 'Edible gold leaf'),
        ('Peanut butter cups', 'Marshmallows'),
        ('Teddy bears', 'Lucky charms'),
    )

    occasion = forms.ChoiceField(choices=OCCASION_CHOICES)
    servingSize = forms.ChoiceField(choices=SERVING_SIZE_CHOICES)
    flavor = forms.ChoiceField(choices=FLAVOR_CHOICES)
    toppings = forms.ChoiceField(choices=TOPPINGS_CHOICES)
    cardMessage = forms.CharField(max_length=255)

    class Meta:
        model = Cake
        fields = [
            'occasion', 'servingSize',
            'flavor', 'toppings', 'cardMessage'
        ]

    # gives all the fields the class of input
    def __init__(self, *args, **kwargs):
        super(CakeForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
