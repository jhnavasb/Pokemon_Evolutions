from django.db import models


class chain(models.Model):

    id = models.IntegerField(primary_key=True)

    def __str__(self):
        return "Chain #%d" % (self.id)


class pokemon(models.Model):

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    height = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)
    hp = models.IntegerField(default=0)
    attack = models.IntegerField(default=0)
    defense = models.IntegerField(default=0)
    special_attack = models.IntegerField(default=0)
    special_defense = models.IntegerField(default=0)
    speed = models.IntegerField(default=0)
    rank = models.IntegerField(default=0)

    evo_chain = models.ForeignKey(
        chain,
        related_name='pokemon',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return "%d - %s" % (self.id, self.name)
