from django.db import models


# Create your models here.
class Hero(models.Model):
    TYPE_CHOICE = (
        (0, "STRENGTH"),
        (1, "AGILITY"),
        (2, "INTELLIGENCE"),
    )

    hero_id = models.AutoField(primary_key=True)
    bio = models.TextField()
    name = models.TextField(null=False)
    type = models.SmallIntegerField(choices=TYPE_CHOICE)
    health = models.IntegerField(null=False)
    damage = models.IntegerField(null=False)
    mana = models.IntegerField(null=False)
    image_url = models.TextField()


class HeroBadAgainst(models.Model):
    hero_1 = models.ForeignKey(Hero, on_delete=models.CASCADE, related_name="bad_against_target_hero")
    hero_2 = models.ForeignKey(Hero, on_delete=models.CASCADE, related_name="bad_against_hero")


class HeroBestCombos(models.Model):
    hero_1 = models.ForeignKey(Hero, on_delete=models.CASCADE, related_name="best_combos_target_hero")
    hero_2 = models.ForeignKey(Hero, on_delete=models.CASCADE, related_name="best_combos_hero")


class HeroGoodAgainst(models.Model):
    hero_1 = models.ForeignKey(Hero, on_delete=models.CASCADE, related_name="good_against_target_hero")
    hero_2 = models.ForeignKey(Hero, on_delete=models.CASCADE, related_name="good_against_hero")
