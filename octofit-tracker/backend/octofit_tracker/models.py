from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='members')

    def __str__(self):
        return self.name

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    type = models.CharField(max_length=100)
    duration = models.IntegerField()  # in minutes
    date = models.DateField()

    def __str__(self):
        return f"{self.type} by {self.user.name} on {self.date}"

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    suggested_for = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Leaderboard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()

    def __str__(self):
        return f"{self.user.name}: {self.score}"
