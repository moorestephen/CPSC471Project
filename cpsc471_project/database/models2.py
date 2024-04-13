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
    group = models.ForeignKey(AuthGroup, on_delete=models.CASCADE)
    permission = models.ForeignKey('AuthPermission', on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', on_delete=models.CASCADE)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
    group = models.ForeignKey(AuthGroup, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
    permission = models.ForeignKey(AuthPermission, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DatabaseAdmin(models.Model):
    email = models.CharField(primary_key=True, max_length=254)
    tenure_start = models.DateField()
    fname = models.CharField(max_length=15)
    lname = models.CharField(max_length=30)
    club_name = models.ForeignKey('DatabaseClub', on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'database_admin'


class DatabaseClub(models.Model):
    name = models.CharField(primary_key=True, max_length=100)
    city = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'database_club'


class DatabaseCoach(models.Model):
    email = models.CharField(primary_key=True, max_length=254)
    tenure_start = models.DateField()
    contract_start = models.DateField()
    fname = models.CharField(max_length=15)
    lname = models.CharField(max_length=30)
    club = models.ForeignKey(DatabaseClub, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'database_coach'


class DatabaseCompetition(models.Model):
    name = models.CharField(primary_key=True, max_length=100)
    sanctioned = models.BooleanField()
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'database_competition'


class DatabaseCompetitioncoachdelegations(models.Model):
    coach = models.ForeignKey(DatabaseCoach, on_delete=models.CASCADE)
    competition = models.ForeignKey(DatabaseCompetition, on_delete=models.CASCADE)
    delegating_admin = models.ForeignKey(DatabaseAdmin, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'database_competitioncoachdelegations'


class DatabaseCompetitionswimmersattending(models.Model):
    competition = models.ForeignKey(DatabaseCompetition, on_delete=models.CASCADE)
    swimmer = models.ForeignKey('DatabaseSwimmer', on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'database_competitionswimmersattending'


class DatabaseEntry(models.Model):
    entry_time = models.TimeField()
    final_time = models.PositiveIntegerField()
    swimmer = models.ForeignKey('DatabaseSwimmer', on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'database_entry'


class DatabaseEvent(models.Model):
    distance = models.PositiveIntegerField()
    stroke = models.CharField(max_length=30)
    course = models.CharField(max_length=20)
    competition = models.ForeignKey(DatabaseCompetition, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'database_event'


class DatabaseEventrecord(models.Model):
    entry_time = models.TimeField()
    final_time_seconds = models.PositiveIntegerField()
    distance = models.PositiveIntegerField()
    stroke = models.CharField(max_length=30)
    course = models.CharField(max_length=20)
    competition = models.ForeignKey(DatabaseCompetition, on_delete=models.CASCADE)
    swimmer = models.ForeignKey('DatabaseSwimmer', on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'database_eventrecord'


class DatabaseGroup(models.Model):
    name = models.CharField(primary_key=True, max_length=100)
    monthly_fee = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    club = models.ForeignKey(DatabaseClub, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'database_group'


class DatabaseGroupcoaches(models.Model):
    coach = models.ForeignKey(DatabaseCoach,  on_delete=models.CASCADE)
    group = models.ForeignKey(DatabaseGroup, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'database_groupcoaches'


class DatabaseGrouppractices(models.Model):
    day = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    group = models.ForeignKey(DatabaseGroup, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'database_grouppractices'


class DatabaseSwimmer(models.Model):
    email = models.CharField(primary_key=True, unique=True, max_length=254)
    dob = models.DateField()
    fname = models.CharField(max_length=15)
    lname = models.CharField(max_length=30)
    club = models.ForeignKey(DatabaseClub, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'database_swimmer'


class DatabaseSwimmergroup(models.Model):
    group = models.ForeignKey(DatabaseGroup,  on_delete=models.CASCADE)
    swimmer = models.ForeignKey(DatabaseSwimmer,  on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'database_swimmergroup'


class DjangoAdminLog(models.Model):
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
    action_time = models.DateTimeField()

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
