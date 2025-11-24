from django.shortcuts import render, redirect
from django.conf import settings
from .models import Shipment, Estimate, ShipmentEvent
import urllib.parse

# home
def home(request):
    return render(request, "website/home.html")


# tracking view — shows shipment + timeline events (oldest -> newest)
def tracking(request):
    code = request.GET.get("code") or request.GET.get("tracking_number")
    shipment = None
    events = None
    searched = False

    if code:
        searched = True
        shipment = Shipment.objects.filter(tracking_number__iexact=code).first()
        if shipment:
            # events newest-first in DB; reverse for timeline reading order
            events = shipment.events.all().order_by('timestamp')

    return render(request, "website/tracking.html", {
        "shipment": shipment,
        "events": events,
        "searched": searched,
    })


# shipment calculator (keeps your logic)
def calculator(request):
    result = None
    breakdown = None
    wa_message = None

    rates = {
        'USD': 1.0,
        'EUR': 0.87,
        'GBP': 0.78
    }

    if request.method == "POST":
        phone = request.POST.get("phone")
        try:
            weight = float(request.POST.get("weight", 0))
        except:
            weight = 0.0
        try:
            distance = float(request.POST.get("distance", 0))
        except:
            distance = 0.0

        delivery_type = request.POST.get("delivery_type", "standard")
        currency = request.POST.get("currency", "USD")

        weight_cost = weight * 5.0
        distance_cost = distance * 0.4
        base_cost = weight_cost + distance_cost

        multiplier = 1.0
        if delivery_type == "express":
            multiplier = 1.4

        total_usd = round(base_cost * multiplier, 2)
        rate = rates.get(currency, 1.0)
        displayed_price = round(total_usd * rate, 2)

        breakdown = {
            'weight_cost_usd': round(weight_cost, 2),
            'distance_cost_usd': round(distance_cost, 2),
            'multiplier': multiplier,
            'total_usd': total_usd,
            'currency': currency,
            'displayed_price': displayed_price,
            'rate': rate
        }

        est = Estimate.objects.create(
            weight_kg=weight,
            distance_km=distance,
            delivery_type=delivery_type,
            currency=currency,
            price=displayed_price,
            phone=phone,
            note=f"Calculated from USD {total_usd}"
        )

        result = displayed_price

        wa_message = (
            f"Hello Pioneer Global Logistics,\n"
            f"I'd like a formal quote for a shipment:\n"
            f"- Phone: {phone}\n"
            f"- Weight: {weight} kg\n"
            f"- Distance: {distance} km\n"
            f"- Service: {delivery_type}\n"
            f"- Estimated price: {displayed_price} {currency}\n"
            f"Please advise next steps."
        )

    return render(request, "website/calculator.html", {
        "result": result,
        "breakdown": breakdown,
        "wa_message": wa_message
    })


def estimate_lookup(request):
    results = None
    if request.method == "POST":
        phone = request.POST.get("phone")
        results = Estimate.objects.filter(phone=phone).order_by("-created_at")
    return render(request, "website/estimate_lookup.html", {
        "results": results
    })


def services(request):
    return render(request, "website/services.html")


def contact(request):
    return render(request, "website/contact.html")


def about(request):
    return render(request, "website/about.html")
