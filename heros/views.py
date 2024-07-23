from rest_framework import viewsets
from django.shortcuts import render, get_object_or_404
from .models import Hero, Tank, DamageDealer, Support, Counter
from .serializers import HeroSerializer, TankSerializer, DamageDealerSerializer, SupportSerializer, CounterSerializer

class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer

class TankViewSet(viewsets.ModelViewSet):
    queryset = Tank.objects.all()
    serializer_class = TankSerializer



class DamageDealerViewSet(viewsets.ModelViewSet):
    queryset = DamageDealer.objects.all()
    serializer_class = DamageDealerSerializer

class SupportViewSet(viewsets.ModelViewSet):
    queryset = Support.objects.all()
    serializer_class = SupportSerializer

class CounterViewSet(viewsets.ModelViewSet):
    queryset = Counter.objects.all()
    serializer_class = CounterSerializer

def character_list(request):
    tanks = Tank.objects.all()
    damage_dealers = DamageDealer.objects.all()
    supports = Support.objects.all()
    return render(request, 'character_list.html', {
        'tanks': tanks,
        'damage_dealers': damage_dealers,
        'supports': supports
    })

def tank_detail(request, pk):
    tank = get_object_or_404(Tank, pk=pk)
    counters = Counter.objects.filter(hero=tank)
    countered_by = Counter.objects.filter(countered_hero=tank)
    damage_dealers = DamageDealer.objects.all()
    supports = Support.objects.all()
    tanks = Tank.objects.all()
    return render(request, 'tank_detail.html', {
        'tank': tank,
        'counters': counters,
        'countered_by': countered_by,
        'damage_dealers': damage_dealers,
        'supports': supports,
        'tanks': tanks,
    })

def dd_detail(request, pk):
    damage_dealer = get_object_or_404(DamageDealer, pk=pk)
    counters = Counter.objects.filter(hero=damage_dealer)
    damage_dealers = DamageDealer.objects.all()
    supports = Support.objects.all()
    tanks = Tank.objects.all()
    countered_by = Counter.objects.filter(countered_hero=damage_dealer)
    return render(request, 'damagedealer_detail.html', {
        'damage_dealer': damage_dealer,
        'counters': counters,
        'countered_by': countered_by,
        'damage_dealers': damage_dealers,
        'supports': supports,
        'tanks': tanks,
    })

def support_detail(request, pk):
    support = get_object_or_404(Support, pk=pk)
    counters = Counter.objects.filter(hero=support)
    countered_by = Counter.objects.filter(countered_hero=support)
    damage_dealers = DamageDealer.objects.all()
    supports = Support.objects.all()
    tanks = Tank.objects.all()
    return render(request, 'support_detail.html', {
        'support': support,
        'counters': counters,
        'countered_by': countered_by,
        'damage_dealers': damage_dealers,
        'supports': supports,
        'tanks': tanks,
    })

