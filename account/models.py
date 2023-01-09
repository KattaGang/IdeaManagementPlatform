from django.db import models
from django.contrib.auth.models import User
from program.models import Program, BusinessUnit
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    city = models.CharField(max_length=200, null=True, default='Not Specified')
    state = models.CharField(max_length=200, null=True,
                             default='Not Specified')
    country = models.CharField(
        max_length=200, null=True, default='Not Specified')
    is_jury = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    department = models.CharField(max_length=200, null=True, blank=True)
    field_of_work = models.CharField(max_length=200, null=True, blank=True)
    years_of_experience = models.DurationField(null=True, blank=True)

    jury_programs = models.ManyToManyField(Program, blank=True)
    jury_business_unit = models.ForeignKey(BusinessUnit, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.user.username
