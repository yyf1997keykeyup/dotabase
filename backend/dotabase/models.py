# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CorsheadersCorsmodel(models.Model):
    cors = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'corsheaders_corsmodel'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class ProjActiveeffect(models.Model):
    effectid = models.OneToOneField('ProjEffect', models.DO_NOTHING, db_column='EffectID', primary_key=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=255)  # Field name made lowercase.
    mana = models.CharField(db_column='Mana', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'proj_ActiveEffect'


class ProjEffect(models.Model):
    effictid = models.IntegerField(db_column='EffictID', primary_key=True)  # Field name made lowercase.
    cd = models.CharField(db_column='CD', max_length=255)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'proj_Effect'


class ProjHero(models.Model):
    heroid = models.IntegerField(db_column='HeroID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=255)  # Field name made lowercase.
    attr_health = models.CharField(db_column='Attr_Health', max_length=20)  # Field name made lowercase.
    attr_damage = models.CharField(db_column='Attr_Damage', max_length=20)  # Field name made lowercase.
    attr_mana = models.CharField(db_column='Attr_Mana', max_length=20)  # Field name made lowercase.
    imageurl = models.CharField(db_column='ImageUrl', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bio = models.CharField(db_column='Bio', max_length=5000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'proj_Hero'


class ProjHerobadagainst(models.Model):
    heroid_1 = models.OneToOneField(ProjHero, models.DO_NOTHING, db_column='HeroID_1', primary_key=True)  # Field name made lowercase.
    heroid_2 = models.ForeignKey(ProjHero, models.DO_NOTHING, db_column='HeroID_2',related_name='bad_against')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'proj_HeroBadAgainst'
        unique_together = (('heroid_1', 'heroid_2'),)


class ProjHerobestcombos(models.Model):
    heroid_1 = models.OneToOneField(ProjHero, models.DO_NOTHING, db_column='HeroID_1', primary_key=True)  # Field name made lowercase.
    heroid_2 = models.ForeignKey(ProjHero, models.DO_NOTHING, db_column='HeroID_2',related_name='best_combos')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'proj_HeroBestCombos'
        unique_together = (('heroid_1', 'heroid_2'),)


class ProjHerogoodagainst(models.Model):
    heroid_1 = models.OneToOneField(ProjHero, models.DO_NOTHING, db_column='HeroID_1', primary_key=True)  # Field name made lowercase.
    heroid_2 = models.ForeignKey(ProjHero, models.DO_NOTHING, db_column='HeroID_2', related_name='good_against')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'proj_HeroGoodAgainst'
        unique_together = (('heroid_1', 'heroid_2'),)


class ProjHeroSkill(models.Model):
    heroid = models.OneToOneField(ProjHero, models.DO_NOTHING, db_column='HeroID', primary_key=True)  # Field name made lowercase.
    skillid = models.ForeignKey('ProjSkill', models.DO_NOTHING, db_column='SkillID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'proj_Hero_Skill'
        unique_together = (('heroid', 'skillid'),)


class ProjHeroTalent(models.Model):
    heroid = models.IntegerField(db_column='HeroID')  # Field name made lowercase.
    talentid = models.IntegerField(db_column='TalentID')  # Field name made lowercase.
    level = models.IntegerField(db_column='Level')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'proj_Hero_Talent'


class ProjItem(models.Model):
    itemid = models.IntegerField(db_column='ItemID', primary_key=True)  # Field name made lowercase.
    itemname = models.CharField(db_column='ItemName', max_length=255)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=255)  # Field name made lowercase.
    bonus = models.CharField(db_column='Bonus', max_length=255)  # Field name made lowercase.
    cost = models.CharField(db_column='Cost', max_length=255)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255)  # Field name made lowercase.
    shop = models.CharField(db_column='Shop', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'proj_Item'


class ProjItemEffect(models.Model):
    itemid = models.OneToOneField(ProjItem, models.DO_NOTHING, db_column='ItemID', primary_key=True)  # Field name made lowercase.
    effectid = models.ForeignKey(ProjEffect, models.DO_NOTHING, db_column='EffectID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'proj_Item_Effect'


class ProjItemRecipe(models.Model):
    itemid_1 = models.OneToOneField(ProjItem, models.DO_NOTHING, db_column='ItemID_1', primary_key=True)  # Field name made lowercase.
    itemid_2 = models.ForeignKey(ProjItem, models.DO_NOTHING, db_column='ItemID_2', related_name='item_recipe')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'proj_Item_Recipe'
        unique_together = (('itemid_1', 'itemid_2'),)


class ProjItemRecommend(models.Model):
    heroid = models.OneToOneField(ProjHero, models.DO_NOTHING, db_column='HeroID', primary_key=True)  # Field name made lowercase.
    itemid = models.ForeignKey(ProjItem, models.DO_NOTHING, db_column='ItemID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'proj_Item_Recommend'
        unique_together = (('heroid', 'itemid'),)


class ProjPassiveeffect(models.Model):
    peffectid = models.OneToOneField(ProjEffect, models.DO_NOTHING, db_column='PEffectID', primary_key=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=255)  # Field name made lowercase.
    mana = models.CharField(db_column='Mana', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'proj_PassiveEffect'


class ProjSkill(models.Model):
    skillid = models.IntegerField(db_column='SkillID', primary_key=True)  # Field name made lowercase.
    skillname = models.CharField(db_column='SkillName', max_length=255)  # Field name made lowercase.
    imageurl = models.CharField(db_column='ImageUrl', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=1024)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'proj_Skill'


class ProjSkillEffect(models.Model):
    skillid = models.OneToOneField(ProjSkill, models.DO_NOTHING, db_column='SkillID', primary_key=True)  # Field name made lowercase.
    effectid = models.ForeignKey(ProjEffect, models.DO_NOTHING, db_column='EffectID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'proj_Skill_Effect'


class ProjTalent(models.Model):
    talentid = models.IntegerField(db_column='TalentID', primary_key=True)  # Field name made lowercase.
    talentname = models.CharField(db_column='TalentName', max_length=255)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'proj_Talent'


class ProjHeroLog(models.Model):
    hero_id = models.IntegerField()
    attr_health = models.CharField(db_column='Attr_Health', max_length=255, blank=True, null=True)  # Field name made lowercase.
    attr_damage = models.CharField(db_column='Attr_Damage', max_length=255, blank=True, null=True)  # Field name made lowercase.
    attr_maga = models.CharField(db_column='Attr_Maga', max_length=255, blank=True, null=True)  # Field name made lowercase.
    create_time = models.DateTimeField(db_column='Create_Time', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'proj_hero_log'
