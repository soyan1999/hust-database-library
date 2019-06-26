from django.db import models
from django.contrib.auth.models import User


class Ticket(models.Model):
    price = models.DecimalField(max_digits=6, decimal_places=2)
    time = models.DateTimeField()
    state = models.SmallIntegerField(default=0)
    description = models.CharField(max_length=150)
    reader = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="ticket_reader_id")

    def __str__(self):
        return self.description


class Book(models.Model):
    name = models.CharField(max_length=150)
    publish = models.CharField(max_length=150)
    time = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        unique_together = ("name", "publish", "time", "price")

    def __str__(self):
        return self.name


class Write(models.Model):
    writer = models.CharField(max_length=150)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return self.writer

    class Meta:
        unique_together = ("writer", "book")


class Store(models.Model):
    location = models.CharField(max_length=150)
    state = models.SmallIntegerField(default=1)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return self.location


class Loan(models.Model):
    time = models.DateTimeField()
    state = models.SmallIntegerField(default=0)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    reader = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="loan_reader_id")
