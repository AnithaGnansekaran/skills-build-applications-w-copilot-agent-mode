from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Team, User, Activity, Workout, Leaderboard

class APISmokeTest(APITestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team')
        self.user = User.objects.create(name='Test User', email='test@example.com', team=self.team)
        self.workout = Workout.objects.create(name='Test Workout', description='desc', suggested_for='Test')
        self.activity = Activity.objects.create(user=self.user, type='Test', duration=10, date='2023-01-01')
        self.leaderboard = Leaderboard.objects.create(user=self.user, score=42)

    def test_api_root(self):
        url = reverse('api-root')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_users_endpoint(self):
        url = reverse('user-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_teams_endpoint(self):
        url = reverse('team-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_activities_endpoint(self):
        url = reverse('activity-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_workouts_endpoint(self):
        url = reverse('workout-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_leaderboard_endpoint(self):
        url = reverse('leaderboard-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
