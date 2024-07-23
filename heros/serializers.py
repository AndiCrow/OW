from rest_framework import serializers
from .models import Hero, Tank, DamageDealer, Support, Counter

class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = ['id', 'name', 'weapon', 'background_story', 'first_ability', 'second_ability', 'third_ability', 'ulti']

class TankSerializer(HeroSerializer):
    class Meta(HeroSerializer.Meta):
        model = Tank

class DamageDealerSerializer(HeroSerializer):
    class Meta(HeroSerializer.Meta):
        model = DamageDealer

class SupportSerializer(HeroSerializer):
    class Meta(HeroSerializer.Meta):
        model = Support

class CounterSerializer(serializers.ModelSerializer):
    hero = HeroSerializer()
    countered_hero = HeroSerializer()

    class Meta:
        model = Counter
        fields = ['id', 'hero', 'countered_hero']

    def create(self, validated_data):
        hero_data = validated_data.pop('hero')
        countered_hero_data = validated_data.pop('countered_hero')

        hero, created = Hero.objects.get_or_create(**hero_data)
        countered_hero, created = Hero.objects.get_or_create(**countered_hero_data)

        counter = Counter.objects.create(hero=hero, countered_hero=countered_hero)
        return counter

    def update(self, instance, validated_data):
        hero_data = validated_data.pop('hero')
        countered_hero_data = validated_data.pop('countered_hero')

        hero, created = Hero.objects.get_or_create(**hero_data)
        countered_hero, created = Hero.objects.get_or_create(**countered_hero_data)

        instance.hero = hero
        instance.countered_hero = countered_hero
        instance.save()

        return instance
