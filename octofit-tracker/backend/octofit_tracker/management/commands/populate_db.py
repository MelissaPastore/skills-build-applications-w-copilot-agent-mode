from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.conf import settings
from pymongo import MongoClient
from datetime import timedelta, datetime
from bson import ObjectId

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB
        client = MongoClient(settings.DATABASES['default']['HOST'], settings.DATABASES['default']['PORT'])
        db = client[settings.DATABASES['default']['NAME']]

        # Ensure database collections are cleared properly
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create users
        users = [
            User(id=ObjectId(), email='thundergod@mhigh.edu', name='Thunder God', created_at=datetime.now()),
            User(id=ObjectId(), email='metalgeek@mhigh.edu', name='Metal Geek', created_at=datetime.now()),
            User(id=ObjectId(), email='zerocool@mhigh.edu', name='Zero Cool', created_at=datetime.now()),
            User(id=ObjectId(), email='crashoverride@mhigh.edu', name='Crash Override', created_at=datetime.now()),
            User(id=ObjectId(), email='sleeptoken@mhigh.edu', name='Sleep Token', created_at=datetime.now()),
        ]
        User.objects.bulk_create(users)

        # Create teams
        teams = [
            Team(id=ObjectId(), name='Blue Team'),
            Team(id=ObjectId(), name='Gold Team')
        ]
        Team.objects.bulk_create(teams)
        # Correctly populate the members field for teams
        for team in teams:
            team.members.clear()  # Clear any existing members
            for user in users:
                team.members.add(user)  # Add each user to the team
            team.save()

        # Create activities
        activities = [
            Activity(id=ObjectId(), user=users[0], type='Cycling', duration=60),
            Activity(id=ObjectId(), user=users[1], type='Crossfit', duration=120),
            Activity(id=ObjectId(), user=users[2], type='Running', duration=90),
            Activity(id=ObjectId(), user=users[3], type='Strength', duration=30),
            Activity(id=ObjectId(), user=users[4], type='Swimming', duration=75),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(id=ObjectId(), team=teams[0], points=100),
            Leaderboard(id=ObjectId(), team=teams[1], points=90),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(id=ObjectId(), name='Cycling Training', description='Training for a road cycling event'),
            Workout(id=ObjectId(), name='Crossfit', description='Training for a crossfit competition'),
            Workout(id=ObjectId(), name='Running Training', description='Training for a marathon'),
            Workout(id=ObjectId(), name='Strength Training', description='Training for strength'),
            Workout(id=ObjectId(), name='Swimming Training', description='Training for a swimming competition'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))