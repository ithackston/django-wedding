from django.db import models

class Wedding(models.Model):
    title = models.CharField(max_length=200)
    root = models.BooleanField(default=False)

class Campaign(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    end_date = models.DateTimeField()

class Invite(models.Model):
    campaign = models.ForeignKey(Campaign)
    code = models.CharField(max_length=64)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    max_add = models.IntegerField(default=0)

class Meal(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)

class Response(models.Model):
    invite = models.ForeignKey(Invite)
    date = models.DateTimeField(auto_now=False, auto_now_add=True)

class Attendee(models.Model):
    response = models.ForeignKey(Response)
    attending = models.BooleanField(default=False)
    meal = models.ForeignKey(Meal)
    note = models.TextField(null=True)
