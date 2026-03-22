from django.core.management.base import BaseCommand
from octofit_tracker.models import Team, User, Activity, Workout, Leaderboard
from django.db import connection
from pymongo import MongoClient
from datetime import date

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear all data
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Users
        users = [
            User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
            User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel),
            User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
            User.objects.create(name='Batman', email='batman@dc.com', team=dc),
        ]

        # Activities
        Activity.objects.create(user=users[0], type='Running', duration=30, date=date(2023, 1, 1))
        Activity.objects.create(user=users[1], type='Cycling', duration=45, date=date(2023, 1, 2))
        Activity.objects.create(user=users[2], type='Swimming', duration=60, date=date(2023, 1, 3))
        Activity.objects.create(user=users[3], type='Yoga', duration=40, date=date(2023, 1, 4))

        # Workouts
        Workout.objects.create(name='Hero HIIT', description='High intensity for heroes', suggested_for='Marvel')
        Workout.objects.create(name='Gotham Strength', description='Strength for Gotham defenders', suggested_for='DC')

        # Leaderboard
        Leaderboard.objects.create(user=users[0], score=100)
        Leaderboard.objects.create(user=users[1], score=90)
        Leaderboard.objects.create(user=users[2], score=95)
        Leaderboard.objects.create(user=users[3], score=85)

        # Ensure unique index on email
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']
        db.user.create_index('email', unique=True)
        self.stdout.write(self.style.SUCCESS('Database populated with test data.'))
