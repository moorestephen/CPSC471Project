from .models import (Club, Swimmer, Group, SwimmerGroup, Coach, GroupCoaches, Admin,
                     GroupPractices, Competition, CompetitionCoachDelegations, 
                     CompetitionSwimmersAttending, EventRecord, Event, Entry)
from .serializers import (ClubSerializer, SwimmerSerializer, GroupSerializer, SwimmerGroupSerializer,
                          CoachSerializer, GroupCoachesSerializer, AdminSerializer, GroupPracticesSerializer,
                          CompetitionSerializer, CompetitionCoachDelegationsSerializer, CompetitionSwimmersAttendingSerializer,
                          EventRecordSerializer, EventSerializer, EntrySerializer)

from rest_framework import generics

class ClubListCreate(generics.ListCreateAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer

class ClubRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer

class SwimmerListCreate(generics.ListCreateAPIView):
    queryset = Swimmer.objects.all()
    serializer_class = SwimmerSerializer

class SwimmerRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Swimmer.objects.all()
    serializer_class = SwimmerSerializer

class GroupListCreate(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class GroupRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class SwimmerGroupListCreate(generics.ListCreateAPIView):
    queryset = SwimmerGroup.objects.all()
    serializer_class = SwimmerGroupSerializer

class SwimmerGroupRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = SwimmerGroup.objects.all()
    serializer_class = SwimmerGroupSerializer

class CoachListCreate(generics.ListCreateAPIView):
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer

class CoachRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer

class GroupCoachesListCreate(generics.ListCreateAPIView):
    queryset = GroupCoaches.objects.all()
    serializer_class = GroupCoachesSerializer

class GroupCoachesRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = GroupCoaches.objects.all()
    serializer_class = GroupCoachesSerializer

class AdminListCreate(generics.ListCreateAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer

class AdminRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer

class GroupPracticesListCreate(generics.ListCreateAPIView):
    queryset = GroupPractices.objects.all()
    serializer_class = GroupPracticesSerializer

class GroupPracticesRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = GroupPractices.objects.all()
    serializer_class = GroupPracticesSerializer

class CompetitionListCreate(generics.ListCreateAPIView):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer

class CompetitionRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer

class CompetitionCoachDelegationsListCreate(generics.ListCreateAPIView):
    queryset = CompetitionCoachDelegations.objects.all()
    serializer_class = CompetitionCoachDelegationsSerializer

class CompetitionCoachDelegationsRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = CompetitionCoachDelegations.objects.all()
    serializer_class = CompetitionCoachDelegationsSerializer

class CompetitionSwimmersAttendingListCreate(generics.ListCreateAPIView):
    queryset = CompetitionSwimmersAttending.objects.all()
    serializer_class = CompetitionSwimmersAttendingSerializer

class CompetitionSwimmersAttendingRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = CompetitionSwimmersAttending.objects.all()
    serializer_class = CompetitionSwimmersAttendingSerializer

class EventRecordListCreate(generics.ListCreateAPIView):
    queryset = EventRecord.objects.all()
    serializer_class = EventRecordSerializer

class EventRecordRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = EventRecord.objects.all()
    serializer_class = EventRecordSerializer

class EventListCreate(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EntryListCreate(generics.ListCreateAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer

class EntryRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer