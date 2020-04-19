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


# TODO: 关系类是否需要设置联合主键
class HeroBadAgainst(models.Model):
    hero_1 = models.ForeignKey(Hero, on_delete=models.CASCADE, related_name="bad_against_target_hero")
    hero_2 = models.ForeignKey(Hero, on_delete=models.CASCADE, related_name="bad_against_hero")
    class Meta:
        unique_together = ('hero_1', 'hero_2')


class HeroBestCombos(models.Model):
    hero_1 = models.ForeignKey(Hero, on_delete=models.CASCADE, related_name="best_combos_target_hero")
    hero_2 = models.ForeignKey(Hero, on_delete=models.CASCADE, related_name="best_combos_hero")
    class Meta:
        unique_together = ('hero_1', 'hero_2')


class HeroGoodAgainst(models.Model):
    hero_1 = models.ForeignKey(Hero, on_delete=models.CASCADE, related_name="good_against_target_hero")
    hero_2 = models.ForeignKey(Hero, on_delete=models.CASCADE, related_name="good_against_hero")
    class Meta:
        unique_together = ('hero_1', 'hero_2')


class Effect(models.Model):
    effect_id = models.AutoField(primary_key=True)
    cd = models.TextField(null=False)
    description = models.TextField()


class ActiveEffect(models.Model):
    effect_id = models.IntegerField(primary_key=True)
    type = models.TextField(null=False)
    mana = models.IntegerField(null=False)
    effect_id = models.ForeignKey(Effect, on_delete=models.CASCADE, related_name="active_effect")


class PassiveEffect(models.Model):
    effect_id = models.IntegerField(primary_key=True)
    type = models.TextField(null=False)
    mana = models.IntegerField(null=False)
    effect_id = models.ForeignKey(Effect, on_delete=models.CASCADE, related_name="passive_effect")


class Skill(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.TextField(null=False)
    image_url = models.TextField()
    description = models.TextField()


class HeroSkill(models.Model):
    hero_id = models.ForeignKey(Hero, on_delete=models.CASCADE, related_name="hero_skill_hero")
    skill_id = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name="hero_skill_skill")
    class Meta:
        unique_together = ('hero_id', 'skill_id')


class Talent(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(null=False)
    description = models.TextField()


class HeroTalent(models.Model):
    id = models.AutoField(primary_key=True)
    hero_id = models.ForeignKey(Hero, on_delete=models.CASCADE, related_name="hero_talent_hero")
    talent_id = models.ForeignKey(Talent, on_delete=models.CASCADE, related_name="hero_talent_talent")
    level = models.IntegerField(null=False)
    class Meta:
        unique_together = ('hero_id', 'talent_id')



class Item(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(null=False)
    category = models.TextField(null=False)
    bonus = models.TextField(null=False)
    cost = models.TextField(null=False)
    description = models.TextField(null=False)
    shop = models.TextField(null=False)


class ItemEffect(models.Model):
    item_id = models.IntegerField(primary_key=True)
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="item_effect_item")
    effect_id = models.ForeignKey(Effect, on_delete=models.CASCADE, related_name="item_effect_effect")


class ItemRecipe(models.Model):
    item_1 = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="item_recipe_1")
    item_2 = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="item_recipe_2")
    class Meta:
        unique_together = ('item_1', 'item_2')


class ItemRecommend(models.Model):
    hero_id = models.ForeignKey(Hero, on_delete=models.CASCADE, related_name="item_recommend_hero")
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="item_recommend_item")
    class Meta:
        unique_together = ('hero_id', 'item_id')



class SkillEffect(models.Model):
    skill_id = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name="skill_effect_skill")
    effect_id = models.ForeignKey(Effect, on_delete=models.CASCADE, related_name="skill_effect_effect")
    class Meta:
        unique_together = ('skill_id', 'effect_id')



class HeroLog(models.Model):
    id = models.AutoField(primary_key = True)
    hero_id = models.IntegerField(null=False)
    health = models.IntegerField(null=False)
    damage = models.IntegerField(null=False)
    mana = models.IntegerField(null=False)