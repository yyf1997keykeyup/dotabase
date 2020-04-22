# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

#
# class Authuser(models.Model):
#     user_id = models.AutoField(primary_key=True)
#     username = models.CharField(max_length=255)
#     password = models.CharField(max_length=128)
#
#     class Meta:
#         managed = False
#         db_table = 'AuthUser'
#

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


class DotabaseModifyuser(models.Model):
    user_ptr = models.OneToOneField('DotabaseUser', models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'dotabase_modifyuser'


class DotabaseNormaluser(models.Model):
    user_ptr = models.OneToOneField('DotabaseUser', models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'dotabase_normaluser'


class DotabaseSuperuser(models.Model):
    user_ptr = models.OneToOneField('DotabaseUser', models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'dotabase_superuser'


class DotabaseUser(models.Model):
    username = models.CharField(primary_key=True, max_length=20)
    password = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'dotabase_user'


class ProjActiveeffect(models.Model):
    effectid = models.OneToOneField('ProjEffect', models.DO_NOTHING, db_column='EffectID', primary_key=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=255)  # Field name made lowercase.
    mana = models.CharField(db_column='Mana', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'proj_ActiveEffect'


class ProjEffect(models.Model):
    effectid = models.AutoField(db_column='EffectID', primary_key=True)  # Field name made lowercase.
    cd = models.CharField(db_column='CD', max_length=255)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'proj_Effect'


class ProjHero(models.Model):
    heroid = models.AutoField(db_column='HeroID', primary_key=True)  # Field name made lowercase.
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
    heroid_1 = models.ForeignKey(ProjHero, models.DO_NOTHING, db_column='HeroID_1', related_name='bad_against_h1')  # Field name made lowercase.
    heroid_2 = models.ForeignKey(ProjHero, models.DO_NOTHING, db_column='HeroID_2', related_name='bad_against_h2')  # Field name made lowercase.
    hbaid = models.AutoField(db_column='HBAid', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'proj_HeroBadAgainst'


class ProjHerobestcombos(models.Model):
    heroid_1 = models.ForeignKey(ProjHero, models.DO_NOTHING, db_column='HeroID_1', related_name='best_combos_h1')  # Field name made lowercase.
    heroid_2 = models.ForeignKey(ProjHero, models.DO_NOTHING, db_column='HeroID_2', related_name='best_combos_h2')  # Field name made lowercase.
    hbcid = models.AutoField(db_column='HBCid', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'proj_HeroBestCombos'


class ProjHerogoodagainst(models.Model):
    heroid_1 = models.ForeignKey(ProjHero, models.DO_NOTHING, db_column='HeroID_1', related_name='good_against_h1')  # Field name made lowercase.
    heroid_2 = models.ForeignKey(ProjHero, models.DO_NOTHING, db_column='HeroID_2', related_name='good_against_h2')  # Field name made lowercase.
    hgaid = models.AutoField(db_column='HGAid', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'proj_HeroGoodAgainst'


class ProjHeroSkill(models.Model):
    heroid = models.ForeignKey(ProjHero, models.DO_NOTHING, db_column='HeroID')  # Field name made lowercase.
    skillid = models.ForeignKey('ProjSkill', models.DO_NOTHING, db_column='SkillID')  # Field name made lowercase.
    hsid = models.AutoField(db_column='HSid', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'proj_Hero_Skill'


class ProjHeroTalent(models.Model):
    htid = models.AutoField(db_column='HTid', primary_key=True)  # Field name made lowercase.
    heroid = models.ForeignKey(ProjHero, models.DO_NOTHING, db_column='HeroID')  # Field name made lowercase.
    talentid = models.IntegerField(db_column='TalentID')  # Field name made lowercase.
    level = models.IntegerField(db_column='Level')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'proj_Hero_Talent'


class ProjItem(models.Model):
    itemid = models.AutoField(db_column='ItemID', primary_key=True)  # Field name made lowercase.
    itemname = models.CharField(db_column='ItemName', max_length=255)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=255)  # Field name made lowercase.
    imgurl = models.CharField(db_column='ImgUrl', max_length=255, blank=True, null=True)  # Field name made lowercase.
    info = models.CharField(db_column='Info', max_length=16384, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'proj_Item'


class ProjItemEffect(models.Model):
    itemid = models.ForeignKey(ProjItem, models.DO_NOTHING, db_column='ItemID')  # Field name made lowercase.
    effectid = models.ForeignKey(ProjEffect, models.DO_NOTHING, db_column='EffectID')  # Field name made lowercase.
    ieid = models.AutoField(db_column='IEid', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'proj_Item_Effect'


class ProjItemRecipe(models.Model):
    itemid_1 = models.ForeignKey(ProjItem, models.DO_NOTHING, db_column='ItemID_1', related_name='recipe_item1')  # Field name made lowercase.
    itemid_2 = models.ForeignKey(ProjItem, models.DO_NOTHING, db_column='ItemID_2', related_name='recipe_item2')  # Field name made lowercase.
    irpid = models.AutoField(db_column='IRpid', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'proj_Item_Recipe'


class ProjItemRecommend(models.Model):
    heroid = models.ForeignKey(ProjHero, models.DO_NOTHING, db_column='HeroID')  # Field name made lowercase.
    itemid = models.ForeignKey(ProjItem, models.DO_NOTHING, db_column='ItemID')  # Field name made lowercase.
    irdid = models.AutoField(db_column='IRdid', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'proj_Item_Recommend'


class ProjPassiveeffect(models.Model):
    peffectid = models.OneToOneField(ProjEffect, models.DO_NOTHING, db_column='PEffectID', primary_key=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=255)  # Field name made lowercase.
    mana = models.CharField(db_column='Mana', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'proj_PassiveEffect'


class ProjSkill(models.Model):
    skillid = models.AutoField(db_column='SkillID', primary_key=True)  # Field name made lowercase.
    skillname = models.CharField(db_column='SkillName', max_length=255)  # Field name made lowercase.
    imageurl = models.CharField(db_column='ImageUrl', max_length=255, blank=True, null=True)  # Field name made lowercase.
    info = models.CharField(db_column='Info', max_length=16384, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'proj_Skill'


class ProjSkillEffect(models.Model):
    skillid = models.ForeignKey(ProjSkill, models.DO_NOTHING, db_column='SkillID')  # Field name made lowercase.
    effectid = models.ForeignKey(ProjEffect, models.DO_NOTHING, db_column='EffectID')  # Field name made lowercase.
    seid = models.AutoField(db_column='SEid', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'proj_Skill_Effect'


class ProjTalent(models.Model):
    talentid = models.AutoField(db_column='TalentID', primary_key=True)  # Field name made lowercase.
    talentname = models.CharField(db_column='TalentName', max_length=255)  # Field name made lowercase.
    info = models.CharField(db_column='Info', max_length=16384, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'proj_Talent'


class ProjHeroLog(models.Model):
    logid = models.AutoField(db_column='Logid', primary_key=True)  # Field name made lowercase.
    hero = models.ForeignKey(ProjHero, models.DO_NOTHING)
    attr_health = models.CharField(db_column='Attr_Health', max_length=255, blank=True, null=True)  # Field name made lowercase.
    attr_damage = models.CharField(db_column='Attr_Damage', max_length=255, blank=True, null=True)  # Field name made lowercase.
    attr_maga = models.CharField(db_column='Attr_Maga', max_length=255, blank=True, null=True)  # Field name made lowercase.
    create_time = models.DateTimeField(db_column='Create_Time', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'proj_hero_log'
