from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
exercise_types = (
    ('Weight Lifting', 'Weight Lifting'),
    ('Yoga', 'Yoga'),
    ('Bike Ride', 'Bike Ride'),
    ('Run', 'Run'),
    ('Walk', 'Walk'),
    ('Hiit', 'Hiit')
)

body_part_choices = (
    ('Chest + Back', 'Chest + Back'),
    ('Legs', 'Legs'),
    ('Shoulders + Biceps', 'Shoulders + Biceps'),
    ('Shoulders + Triceps', 'Shoulders + Triceps'),
    ('Cardio + Biceps', 'Cardio + Biceps'),
    ('Cardio + Triceps', 'Cardio + Triceps'),
    ('Chest', 'Chest'),
    ('Back', 'Back'),
    ('Shoulders', 'Shoulders'),
    ('Cardio', 'Cardio'),
    ('Biceps', 'Biceps'),
    ('Triceps', 'Triceps')
)

# abstract class
class BaseWorkout(models.Model):
    exercise_string = models.CharField(max_length=30, choices=exercise_types, default='Weight Lifting')
    date = models.DateField(default=timezone.now)
    time_of_day = models.TimeField()
    duration = models.DurationField()
    location = models.CharField(max_length=100)
    mood_before = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    mood_after = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    notes = models.CharField(max_length=100)

    # This makes the class abstract
    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.__class__.__name__} on {self.date}"
    
# lifting exercises
class LiftPost(BaseWorkout):
    body_part = models.CharField(max_length=20, choices=body_part_choices)
    includes_abs = models.BooleanField(default=False)

class LiftPostSet(models.Model):
    workout = models.ForeignKey(LiftPost, on_delete=models.CASCADE)
    workout_name = models.CharField(max_length = 200)
    reps = models.PositiveBigIntegerField(null=True, blank=True)
    weight = models.DecimalField(max_digits = 5, decimal_places=2, null=True, blank=True)
    duration = models.DurationField(null=True, blank=True)
    notes = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f"{self.reps} reps at {self.weight} lbs"

# yoga exercises
class YogaPost(BaseWorkout):
    yoga_type = models.CharField(max_length=200)
    instructor = models.CharField(max_length=200)
    
class YogaPose(models.Model):
    session = models.ForeignKey(YogaPost, related_name='poses', on_delete=models.CASCADE)
    pose_name = models.CharField(max_length=255)
    duration = models.DurationField(null=True, blank=True)

    def __str__(self):
        return self.pose_name
    
# running exercises
class RunningPost(BaseWorkout):
    distance_miles = models.FloatField(validators=[MinValueValidator(0)])
    temperature = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    weather_conditions = models.CharField(max_length=255)
    terrain = models.CharField(max_length=255)

# biking exercises
class BikingPost(BaseWorkout):
    distance_miles = models.FloatField(validators=[MinValueValidator(0)])
    temperature = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    weather_conditions = models.CharField(max_length=255)
    terrain = models.CharField(max_length=255)
    
# Running
class WalkingPost(BaseWorkout):
    distance_miles = models.FloatField(validators=[MinValueValidator(0)])
    temperature = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    weather_conditions = models.CharField(max_length=255)
    terrain = models.CharField(max_length=255)

# HIIT/Other 
class HiitPost(BaseWorkout):
    exercise_label = models.CharField(max_length=200)