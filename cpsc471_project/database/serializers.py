from rest_framework import serializers
from .models import(Club, Swimmer, Group, SwimmerGroup, Coach, GroupCoaches, Admin,
                     GroupPractices, Competition, CompetitionCoachDelegations, 
                     CompetitionSwimmersAttending, EventRecord, Event, Entry)

class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = '__all__'

class SwimmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Swimmer
        fields = '__all__'

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

class SwimmerGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = SwimmerGroup
        fields = '__all__'

class CoachSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coach
        fields = '__all__'

class GroupCoachesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupCoaches
        fields = '__all__'

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'

class GroupPracticesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupPractices
        fields = '__all__'

class CompetitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competition
        fields = '__all__'

class CompetitionCoachDelegationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompetitionCoachDelegations
        fields = '__all__'

class CompetitionSwimmersAttendingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompetitionSwimmersAttending
        fields = '__all__'

class EventRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventRecord
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = '__all__'