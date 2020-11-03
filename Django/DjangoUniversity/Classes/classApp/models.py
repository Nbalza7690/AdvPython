from django.db import models


class DjangoClasses(models.Model):
    Title = models.CharField(max_length=60, default="", blank=True, null=False)
    Course_Number = models.IntegerField(default="", blank=True, null=False)
    Instructor_Name = models.CharField(max_length=60, default="", blank=True, null=False)
    Duration = models.DecimalField(default=0.00, max_digits=10000, decimal_places=2)

    objects = models.Manager()

    def __str__(self):
        return self.Title
