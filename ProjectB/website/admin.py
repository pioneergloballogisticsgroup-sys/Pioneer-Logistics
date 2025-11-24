from django.contrib import admin
from .models import Shipment, ShipmentEvent, Estimate

class ShipmentEventInline(admin.TabularInline):
    model = ShipmentEvent
    extra = 1
    fields = ('timestamp', 'event_type', 'location', 'facility', 'description', 'note')
    ordering = ('-timestamp',)

@admin.register(Shipment)
class ShipmentAdmin(admin.ModelAdmin):
    list_display = ('tracking_number', 'status', 'origin', 'destination', 'last_update')
    search_fields = ('tracking_number', 'sender_name', 'receiver_name', 'origin', 'destination')
    list_filter = ('status', 'service_type')
    inlines = [ShipmentEventInline]
    readonly_fields = ('created_at', 'last_update')

@admin.register(ShipmentEvent)
class ShipmentEventAdmin(admin.ModelAdmin):
    list_display = ('shipment', 'timestamp', 'event_type', 'location', 'facility')
    search_fields = ('shipment__tracking_number', 'description', 'facility', 'location')
    list_filter = ('event_type',)

admin.site.register(Estimate)
