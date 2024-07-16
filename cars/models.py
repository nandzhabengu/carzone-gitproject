from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField

# Create your models here.
class Car(models.Model):
    state_choice = (
        ('AL', 'Alabama'),
        ('AK', 'Alaska'),
        ('AZ', 'Arizona'),
        ('AR', 'Arkansas'),
        ('CA', 'California'),
        ('CO', 'Colorado'),
        ('CT', 'Connecticut'),
        ('DE', 'Delaware'),
        ('DC', 'District Of Columbia'),
        ('FL', 'Florida'),
        ('GA', 'Georgia'),
        ('HI', 'Hawaii'),
        ('ID', 'Idaho'),
        ('IL', 'Illinois'),
        ('IN', 'Indiana'),
        ('IA', 'Iowa'),
        ('KS', 'Kansas'),
        ('KY', 'Kentucky'),
        ('LA', 'Louisiana'),
        ('ME', 'Maine'),
        ('MD', 'Maryland'),
        ('MA', 'Massachusetts'),
        ('MI', 'Michigan'),
        ('MN', 'Minnesota'),
        ('MS', 'Mississippi'),
        ('MO', 'Missouri'),
        ('MT', 'Montana'),
        ('NE', 'Nebraska'),
        ('NV', 'Nevada'),
        ('NH', 'New Hampshire'),
        ('NJ', 'New Jersey'),
        ('NM', 'New Mexico'),
        ('NY', 'New York'),
        ('NC', 'North Carolina'),
        ('ND', 'North Dakota'),
        ('OH', 'Ohio'),
        ('OK', 'Oklahoma'),
        ('OR', 'Oregon'),
        ('PA', 'Pennsylvania'),
        ('RI', 'Rhode Island'),
        ('SC', 'South Carolina'),
        ('SD', 'South Dakota'),
        ('TN', 'Tennessee'),
        ('TX', 'Texas'),
        ('UT', 'Utah'),
        ('VT', 'Vermont'),
        ('VA', 'Virginia'),
        ('WA', 'Washington'),
        ('WV', 'West Virginia'),
        ('WI', 'Wisconsin'),
        ('WY', 'Wyoming'),
    )
    year_choice = []
    for r in range(2000, (datetime.now().year+1)):
        year_choice.append((r,r))

    features_choices = (
        ('Adaptive Cruise Control','Adaptive Cruise Control'),
        ('Audio Interface', 'Audio Interface'),
        ('Airbags', 'Airbags'),
        ('Air Conditioning', 'Air Conditioning'),
        ('Alarm System', 'Alarm System'),
        ('Auto Start/Stop', 'Auto Start/Stop'),
        ('Anti-theft Protection','Anti-theft Protection'),
        ('Automatic Climate Control','Automatic Climate Control'),
        ('Automatic Headlights','Automatic Headlights'),
        ('Bluetooth Handset', 'Bluetooth Handset'),
        ('Bi-Xenon Headlights','Bi-Xenon Headlights'),
        ('BOSE Surround Sound','BOSE Surround Sound'),
        ('Burmester Surround Sound','Burmester Surround Sound'),
        ('Cruise Control', 'Cruise Control'),
        ('CD/DVD Autochanger','CD/DVD Autochanger'),
        ('CDR Audio','CDR Audio'),
        ('Direct Fuel Injection', 'Direct Fuel Injection'),
        ('Electric Parking Brake','Electric Parking Brake'),
        ('Floor Mats','Floor Mats'),
        ('Garage Door Opener','Garage Door Opener'),
        ('Leather Package','Leather Package'),
        ('Locking Rear Differential','Locking Rear Differential'),
        ('Luggage Compartments','Luggage Compartments'),
        ('Manual Transmission','Manual Transmission'),
        ('Navigation Module','Navigation Module'),
        ('Online Services','Online Services'),
        ('Power Steering', 'Power Steering'),
        ('ParkAssist', 'ParkAssist'),
        ('Porsche Communication','Porsche Communication'),
        ('Reversing Camera', 'Reversing Camera'),
        ('Roll-over Protection','Roll-over Protection'),
        ('Seat Heating', 'Seat Heating'),
        ('Seat Ventilation','Seat Ventilation'),
        ('Steering Wheel Heating','Steering Wheel Heating'),
        ('Sound Package Plus','Sound Package Plus'),
        ('Sport Chrono Package','Sport Chrono Package'),
        ('Tire Pressure Monitoring','Tire Pressure Monitoring'),
        ('Universal Audio Interface','Universal Audio Interface'),
        ('Voice Control System','Voice Control System'),
        ('Wind Deflector', 'Wind Deflector'),
    )

    door_choices = (
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    )

    car_title = models.CharField(max_length=255)
    state = models.CharField(choices=state_choice, max_length=100)
    city = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField(('year'),choices=year_choice)
    condition = models.CharField(max_length=100)
    price = models.IntegerField()
    description = RichTextField()
    car_photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    car_photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    car_photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    car_photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    car_photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    features = MultiSelectField(choices=features_choices)
    body_style = models.CharField(max_length=100)
    engine = models.CharField(max_length=100)
    transmission = models.CharField(max_length=100)
    interior = models.CharField(max_length=100)
    miles = models.IntegerField()
    doors = models.CharField(choices=door_choices,max_length=10)
    passengers = models.IntegerField()
    vin_no = models.CharField(max_length=100)
    milage = models.IntegerField()
    fuel_type = models.CharField(max_length=50)
    no_of_owners = models.CharField(max_length=100)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now,blank=True)

    def __str__(self):
        return self.car_title
