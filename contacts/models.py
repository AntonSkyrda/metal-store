from django.db import models


class PhoneNumber(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.IntegerField()

    class Meta:
        ordering = ("name",)
        verbose_name_plural = "Phone Numbers"

    def __str__(self):
        return f"{self.name} {self.phone_number}"


class WorkSchedule(models.Model):
    days = models.CharField(max_length=255)
    hours = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.days} {self.hours}"


class ContactEmail(models.Model):
    email = models.EmailField()

    def __str__(self):
        return f"{self.email}"


class CallBack(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("date", )

    def __str__(self):
        return f"{self.name} {str(self.phone_number)} {str(self.email)}"

