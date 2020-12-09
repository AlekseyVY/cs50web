from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    pass


class Item(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=1024)
    price = models.IntegerField()
    category = models.CharField(max_length=64)
    date = timezone.now()
    url_link = models.CharField(max_length=1024)
    #owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Item_List")


class Bid(models.Model):
    bidder = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Bids")
    Item = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name="Bid")
    bid = models.IntegerField()
    date = timezone.now()

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Comments")
    Item = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name="Comment")
    date = timezone.now()
    comment = models.CharField(max_length=1024)