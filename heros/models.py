from django.db import models



class Hero(models.Model):
    name = models.CharField(max_length=150)
    weapon = models.CharField(max_length=150)
    background_story = models.TextField(blank=True)
    first_ability = models.TextField(blank=True)
    second_ability = models.TextField(blank=True)
    third_ability = models.TextField(blank=True)
    ulti = models.TextField(blank=True)

    class Meta:
        verbose_name = "Hero"
        verbose_name_plural = "Heroes"
        ordering = ["name"]

    def __str__(self):
        return self.name

class Tank(Hero):
    class Meta:
        verbose_name = "Tank"
        verbose_name_plural = "Tanks"
        ordering = ["name"]

class DamageDealer(Hero):
    class Meta:
        verbose_name = "Damage Dealer"
        verbose_name_plural = "Damage Dealers"
        ordering = ["name"]

class Support(Hero):
    class Meta:
        verbose_name = "Support"
        verbose_name_plural = "Supports"
        ordering = ["name"]

class Counter(models.Model):
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE, related_name='counters')
    countered_hero = models.ManyToManyField(Hero, related_name='countered_by')

    class Meta:
        verbose_name = "Counter"
        verbose_name_plural = "Counters"

    def __str__(self):
        return f"{self.hero.name} counters {', '.join([hero.name for hero in self.countered_hero.all()])}"
    