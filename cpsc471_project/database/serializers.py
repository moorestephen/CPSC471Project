from rest_framework import serializers
from .models2 import (DatabaseClub, DatabaseAdmin, DatabaseCoach, DatabaseCompetition,
                      DatabaseCompetitioncoachdelegations, DatabaseCompetitionswimmersattending,
                      DatabaseEntry, DatabaseEvent, DatabaseEventrecord, DatabaseGroup, DatabaseGroupcoaches,
                      DatabaseGrouppractices, DatabaseSwimmer, DatabaseSwimmergroup)

class ClubListSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatabaseClub
        fields = ['name', 'city']

class DatabaseAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatabaseAdmin
        fields = ['email', 'tenure_start', 'fname', 'lname', 'club_name']

class DatabaseCoachSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatabaseCoach
        fields = ['email', 'tenure_start', 'contract_start', 'fname', 'lname', 'club']

class DatabaseCompetitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatabaseCompetition
        fields = ['name', 'sanctioned', 'start_date', 'end_date']

class DatabaseCompetitioncoachdelegationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatabaseCompetitioncoachdelegations
        fields = ['coach', 'competition', 'delegating_admin']

class DatabaseCompetitionswimmersattendingSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatabaseCompetitionswimmersattending
        fields = ['competition', 'swimmer'] 

class DatabaseEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = DatabaseEntry
        fields = ['swimmer', 'event']

class DatabaseEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatabaseEvent
        fields = ['name', 'distance', 'stroke']

class DatabaseEventrecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatabaseEventrecord
        fields = ['entry', 'event', 'time']

class DatabaseGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatabaseGroup
        fields = ['name', 'club']

class DatabaseGroupcoachesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatabaseGroupcoaches
        fields = ['coach', 'group']

class DatabaseGrouppracticesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatabaseGrouppractices
        fields = ['group', 'day', 'time']

class DatabaseSwimmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatabaseSwimmer
        fields = ['email', 'fname', 'lname', 'club']

class DatabaseSwimmergroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatabaseSwimmergroup
        fields = ['swimmer', 'group']