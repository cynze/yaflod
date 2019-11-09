from django.db import models


# Create your models here.

class Family(models.Model):
    class Meta:
        verbose_name_plural = "Families"

    name = models.TextField()

    def __str__(self): return self.name

    # TODO: implement __str__ method


class Flower(models.Model):
    CHOICES = (
        ('y', 'yellow'),
        ('r', 'red'),
        ('g', 'green'),
        ('b', 'blue'),
        ('p', 'purple'),
        ('o', 'orange')
    )

    name = models.TextField()
    color = models.CharField(max_length=1, choices=CHOICES)
    # release_date = models.DateField()
    description = models.TextField()
    growing_duration = models.PositiveIntegerField(help_text="in Weeks")
    family = models.ForeignKey(Family, on_delete=models.CASCADE)
    gardener = models.ManyToManyField('Gardener')

    def __str__(self): return self.name

    # TODO: implement __str__ method


class GardenerManager(models.Manager):

    def duplicates(self):
        # TODO: implement an algorithm to find duplicate entries
        return []


class Gardener(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    year_of_birth = models.IntegerField()

    objects = GardenerManager()

    def __str__(self): return self.first_name

    # TODO: implement __str__ method
