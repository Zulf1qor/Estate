# Generated by Django 5.0.2 on 2024-03-04 12:37

import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('sur_name', models.CharField(max_length=55)),
                ('age', models.CharField(max_length=25)),
                ('phone_number', models.CharField(max_length=13, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_number', message='Invalid phone number', regex='^[\\+]9{2}8{1}[0-9]{9}$')])),
                ('salary', models.PositiveIntegerField()),
                ('status', models.DecimalField(decimal_places=2, max_digits=10)),
                ('hire_date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('sur_name', models.CharField(max_length=55)),
                ('age', models.CharField(max_length=25)),
                ('phone_number', models.CharField(max_length=13, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_number', message='Invalid phone number', regex='^[\\+]9{2}8{1}[0-9]{9}$')])),
                ('password_ser', models.CharField(max_length=155)),
                ('password_number', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lot', models.CharField(max_length=255)),
                ('lat', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('gender', models.CharField(choices=[('Erkak', 'Erkak'), ('Ayol', 'Ayol')], max_length=55)),
                ('phone_number', models.CharField(max_length=13, validators=[django.core.validators.RegexValidator(code='Invalid number', message='Invalide phone number', regex='^[\\+]9{2}8{1}[0-9]{9}$')])),
                ('img', models.ImageField(upload_to='user-imgages/', validators=[django.core.validators.RegexValidator(code='Invalid photos', message='Invalide img ', regex='^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$')])),
                ('bio', models.CharField(max_length=255)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
                'abstract': False,
                'swappable': 'AUTH_USER_MODEL',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='History_contracts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=255)),
                ('date', models.DateTimeField()),
                ('property', models.CharField(max_length=255, verbose_name='enter the property ID')),
                ('contract_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('contract_duration', models.IntegerField()),
                ('agents', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.agents')),
                ('customers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.customers')),
            ],
        ),
        migrations.CreateModel(
            name='Estate',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('rent', models.BooleanField(default=False)),
                ('volume', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('luxurious', 'Luxurious'), ('excellent', 'Excellent'), ('good', 'Good')], default='good', max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('type', models.CharField(choices=[('apartment', 'Apartment'), ('courtyard', 'Courtyard')], max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='estate_photo/', validators=[django.core.validators.RegexValidator(code='invalid_image_format', message='Invalid image format. Supported formats: JPG, JPEG, PNG, GIF, BMP, SVG', regex='image_regex_pattern')])),
                ('rooms', models.IntegerField()),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.location')),
            ],
        ),
        migrations.CreateModel(
            name='Cassa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('total_balance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.location')),
            ],
        ),
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=255)),
                ('img', models.ImageField(blank=True, null=True, upload_to='building_images/')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('volume', models.CharField(max_length=100)),
                ('rooms', models.IntegerField()),
                ('floor', models.IntegerField(blank=True, null=True)),
                ('rent', models.BooleanField(default=False)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.location')),
            ],
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property', models.CharField(max_length=255, verbose_name='enter the property ID')),
                ('date', models.DateTimeField(auto_now=True, verbose_name='Meeting time')),
                ('agents', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.agents')),
                ('customers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.customers')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proproperty', models.CharField(max_length=255, verbose_name='enter the property ID')),
                ('payment_date', models.DateTimeField()),
                ('amount_paid', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.CharField(max_length=255)),
                ('customers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.customers')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentReciept',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reciept', models.ImageField(upload_to='estate_photo/', validators=[django.core.validators.RegexValidator(code='invalid_image_format', message='Invalid image format. Supported formats: JPG, JPEG, PNG, GIF, BMP, SVG', regex='image_regex_pattern')])),
                ('data_issued', models.DateTimeField(auto_now=True)),
                ('payment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.payment')),
            ],
        ),
    ]
