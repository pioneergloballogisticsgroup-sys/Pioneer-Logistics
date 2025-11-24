from django.db import models
from django.utils import timezone

class Shipment(models.Model):
    tracking_number = models.CharField(max_length=50, unique=True)
    sender_name = models.CharField(max_length=150, blank=True)
    sender_address = models.CharField(max_length=300, blank=True)
    receiver_name = models.CharField(max_length=150, blank=True)
    receiver_address = models.CharField(max_length=300, blank=True)

    origin = models.CharField(max_length=200, blank=True)
    destination = models.CharField(max_length=200, blank=True)
    service_type = models.CharField(max_length=80, default="Standard")  # e.g. Air, Sea, Local

    weight_kg = models.FloatField(null=True, blank=True)
    dimensions = models.CharField(max_length=120, blank=True)

    status = models.CharField(max_length=120, default="Pending")
    current_location = models.CharField(max_length=200, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    expected_delivery = models.DateField(null=True, blank=True)
    last_update = models.DateTimeField(auto_now=True)

    notes = models.TextField(blank=True)

    def __str__(self):
        return self.tracking_number

    class Meta:
        ordering = ['-last_update']


class ShipmentEvent(models.Model):
    EVENT_TYPES = [
        ('CREATED', 'Created'),
        ('PICKUP', 'Pickup'),
        ('PROCESSED', 'Processed'),
        ('DEPARTED', 'Departed'),
        ('ARRIVED', 'Arrived'),
        ('CLEARANCE', 'Customs Clearance'),
        ('OUT_FOR_DELIVERY', 'Out for Delivery'),
        ('DELIVERED', 'Delivered'),
        ('OTHER', 'Other'),
    ]

    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE, related_name='events')
    timestamp = models.DateTimeField(default=timezone.now)
    event_type = models.CharField(max_length=30, choices=EVENT_TYPES, default='OTHER')
    location = models.CharField(max_length=200, blank=True)
    facility = models.CharField(max_length=250, blank=True)
    description = models.TextField(blank=True)
    note = models.CharField(max_length=250, blank=True)

    class Meta:
        ordering = ['-timestamp']  # newest first

    def __str__(self):
        return f"{self.timestamp:%Y-%m-%d %H:%M} — {self.get_event_type_display()}"


class Estimate(models.Model):
    weight_kg = models.FloatField()
    distance_km = models.FloatField()
    delivery_type = models.CharField(max_length=50)
    currency = models.CharField(max_length=10)
    price = models.FloatField()
    phone = models.CharField(max_length=20, null=True, blank=True)
    note = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Estimate {self.id} - {self.phone or 'no phone'}"
