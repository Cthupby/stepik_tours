from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseServerError
from .data import title, subtitle, description, departures, tours
import random


def main_view(request):
    rand_tours = random.sample(list(tours.values()), 6)

    context = {
        "title": title,
        "subtitle": subtitle,
        "description": description,
        "departures": departures,
        "tours": rand_tours,
    }
    return render(request, "tours/index.html", context=context)


def departure_view(request, departure):
    tour_deps = {}
    prices = []
    nights = []

    for key, tour in tours.items():
        if tour['departure'] == departure:
            tour_deps[key] = tour
            prices.append(tour['price'])
            nights.append(tour['nights'])

    count = len(tour_deps)
    max_price = max(prices)
    min_price = min(prices)
    max_nights = max(nights)
    min_nights = min(nights)

    context = {
        "title": title,
        "departure": departure,
        "departures": departures,
        "tour_deps": tour_deps,
        "count": count,
        "max_price": max_price,
        "min_price": min_price,
        "max_nights": max_nights,
        "min_nights": min_nights,
    }
    return render(request, "tours/departure.html", context=context)


def tour_view(request, tour_id):
    tour = tours[tour_id]
    departure = departures[tour['departure']]

    context = {
        "title": title,
        "departures": departures,
        "departure": departure,
        "tour": tour,
    }
    return render(request, "tours/tour.html", context=context)


def custom_handler404(request, exception):
    return HttpResponseNotFound('<h2>Страница не найдена.</h2>')


def custom_handler500(request):
    return HttpResponseServerError('<h2>Ошибка сервера.</h2>')
