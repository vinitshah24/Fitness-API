from django.db import models

class Workout(models.Model):
    workout_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)
    created_ts = models.DateTimeField(auto_now=True)
    sets = models.IntegerField(null=False)
    reps = models.IntegerField(null=False)

    def __str__(self):
        return str(self.name)

    class Meta:
        db_table = "workouts"
        managed = False
        ordering = ["workout_id"]
