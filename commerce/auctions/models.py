from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Item(models.Model):
    title = models.CharField(max_length=64)
    decription = models.CharField(max_length=1024)
    price = models.IntegerField()
    date = models.DateField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Item_List")


class Bid(models.Model):
    bidder = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Bids")
    Item = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name="Bid")
    bid = models.IntegerField()
    date = models.DateField()

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Comments")
    Item = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name="Comment")
    date = models.DateField()
    comment = models.CharField(max_length=1024)