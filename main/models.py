from django.db import models


# Create your models here.
class ToDoList(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


"""
class FantasyNames(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
"""


# all items will exist on a to do list
class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    # has the item been completed? returns boolean
    complete = models.BooleanField()

    def __str__(self):
        return self.text
