from django.db import models
from account.models import Profile
from django.contrib.auth.models import User
from program.models import BusinessUnit, Program
from django.utils import timezone
# Create your models here.


class Idea(models.Model):
    STATUS_CHOICES = (
        (0, 'Pending'),
        (1, 'Active'),
        (2, 'Handoff'),
        (3, 'Completed'),
        (4, 'Paused'),
        (5, 'Stopped'),
        (6, 'Put On Hold'),
        (7, 'Rejected'),
    )

    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    summary = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True,
                              upload_to='static/images/')
    business_unit = models.ForeignKey(
        BusinessUnit, null=True, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    ideator = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.SET_NULL)
    program = models.ForeignKey(Program, null=True, on_delete=models.SET_NULL)
    projected_revenue = models.BigIntegerField(null=True)
    actual_net_revenue = models.BigIntegerField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def accept(self):
        self.status = 1

    def reject(self):
        self.status = 6

    def putOnHold(self):
        self.status = 7

    def getStatus(self):
        return self.STATUS_CHOICES[self.status][1]

    class Meta:
        ordering =['-updated', '-created']
