from django.db import models
from django.core.validators import RegexValidator
from django.db.models.signals import post_save
from django.dispatch import receiver


class Estate(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    rent = models.BooleanField(default=False)
    volume = models.CharField(max_length=255)
    STATUS_CHOICES = [
        ('luxurious', 'Luxurious'),
        ('excellent', 'Excellent'),
        ('good', 'Good'),
    ]
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='good')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    TYPE_CHOICES = [
        ('apartment', 'Apartment'),
        ('courtyard', 'Courtyard'),
    ]
    type = models.CharField(max_length=100, choices=TYPE_CHOICES)
    location = models.ForeignKey(to='Location', on_delete=models.PROTECT)
    description = models.TextField()
    image = models.ImageField(upload_to='estate_photo/',
        validators=[
            RegexValidator(
                regex='image_regex_pattern',
                message='Invalid image format. Supported formats: JPG, JPEG, PNG, GIF, BMP, SVG',
                code='invalid_image_format'
            ),])
    rooms = models.IntegerField()

    def count_models(sender, instance, created, **kwargs):
        if created:
            total_models = Estate.objects.count()
            print(f"Total number of Estates: {total_models}")


class Customers(models.Model):
    name = models.CharField(max_length=55)
    sur_name = models.CharField(max_length=55)
    age = models.CharField(max_length=25)
    phone_number = models.CharField(max_length=13, unique=True, validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalid phone number',
            code='invalid_number'

        ), ])
    password_ser = models.CharField(max_length=155)
    password_number = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class Agents(models.Model):
    name = models.CharField(max_length=55)
    sur_name = models.CharField(max_length=55)
    age = models.CharField(max_length=25)
    phone_number = models.CharField(max_length=13, unique=True, validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalid phone number',
            code='invalid_number'

        ), ])
    salary = models.PositiveIntegerField()
    status = models.DecimalField(max_digits=10, decimal_places=2)
    hire_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class Meeting(models.Model):
    customers = models.ForeignKey(to='Customers', on_delete=models.CASCADE)
    agents = models.ForeignKey(to='Agents', on_delete=models.CASCADE)
    property = models.CharField(max_length=255, verbose_name='enter the property ID')
    date = models.DateTimeField(auto_now=True, verbose_name='Meeting time')


class Building(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    location = models.ForeignKey(to='Location', on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    img = models.ImageField(upload_to='building_images/', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    volume = models.CharField(max_length=100)
    rooms = models.IntegerField()
    floor = models.IntegerField(null=True, blank=True)
    rent = models.BooleanField(default=False)

    def count_models(sender, instance, created, **kwargs):
        if created:
            total_models = Building.objects.count()
            print(f"Total number of Buildings: {total_models}")



class History_contracts(models.Model):
    number = models.CharField(max_length=255)
    customers = models.ForeignKey(Customers, on_delete=models.CASCADE)
    agents = models.ForeignKey(Agents, on_delete=models.CASCADE)
    date = models.DateTimeField()
    property = models.CharField(max_length=255, verbose_name='enter the property ID')
    contract_amount = models.DecimalField(max_digits=10, decimal_places=2)
    contract_duration = models.IntegerField()

class Payment(models.Model):
    customers = models.ForeignKey(Customers, on_delete=models.CASCADE)
    proproperty = models.CharField(max_length=255, verbose_name='enter the property ID')
    payment_date = models.DateTimeField()
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255)



class PaymentReciept(models.Model):
    payment = models.ForeignKey(to='Payment', on_delete=models.CASCADE)
    reciept = models.ImageField(upload_to='estate_photo/',
        validators=[
            RegexValidator(
                regex='image_regex_pattern',
                message='Invalid image format. Supported formats: JPG, JPEG, PNG, GIF, BMP, SVG',
                code='invalid_image_format'
            ),])
    data_issued = models.DateTimeField(auto_now=True)


class Cassa(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.ForeignKey(to='Location', on_delete=models.CASCADE)
    total_balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Location(models.Model):
    lot = models.CharField(max_length=255)
    lat = models.CharField(max_length=255)