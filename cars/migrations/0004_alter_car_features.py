# Generated by Django 5.0.6 on 2024-07-24 01:57

import multiselectfield.db.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_alter_car_description_alter_car_features'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='features',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Adaptive Cruise Control', 'Adaptive Cruise Control'), ('Audio Interface', 'Audio Interface'), ('Airbags', 'Airbags'), ('Air Conditioning', 'Air Conditioning'), ('Alarm System', 'Alarm System'), ('Auto Start/Stop', 'Auto Start/Stop'), ('Anti-theft Protection', 'Anti-theft Protection'), ('Automatic Climate Control', 'Automatic Climate Control'), ('Automatic Headlights', 'Automatic Headlights'), ('Bluetooth Handset', 'Bluetooth Handset'), ('Bi-Xenon Headlights', 'Bi-Xenon Headlights'), ('BOSE Surround Sound', 'BOSE Surround Sound'), ('Burmester Surround Sound', 'Burmester Surround Sound'), ('Cruise Control', 'Cruise Control'), ('CD/DVD Autochanger', 'CD/DVD Autochanger'), ('CDR Audio', 'CDR Audio'), ('Direct Fuel Injection', 'Direct Fuel Injection'), ('Electric Parking Brake', 'Electric Parking Brake'), ('Floor Mats', 'Floor Mats'), ('Garage Door Opener', 'Garage Door Opener'), ('Leather Package', 'Leather Package'), ('Locking Rear Differential', 'Locking Rear Differential'), ('Luggage Compartments', 'Luggage Compartments'), ('Manual Transmission', 'Manual Transmission'), ('Navigation Module', 'Navigation Module'), ('Online Services', 'Online Services'), ('Power Steering', 'Power Steering'), ('ParkAssist', 'ParkAssist'), ('Porsche Communication', 'Porsche Communication'), ('Reversing Camera', 'Reversing Camera'), ('Roll-over Protection', 'Roll-over Protection'), ('Seat Heating', 'Seat Heating'), ('Seat Ventilation', 'Seat Ventilation'), ('Steering Wheel Heating', 'Steering Wheel Heating'), ('Sound Package Plus', 'Sound Package Plus'), ('Sport Chrono Package', 'Sport Chrono Package'), ('Tire Pressure Monitoring', 'Tire Pressure Monitoring'), ('Universal Audio Interface', 'Universal Audio Interface'), ('Voice Control System', 'Voice Control System'), ('Wind Deflector', 'Wind Deflector')], max_length=747),
        ),
    ]
