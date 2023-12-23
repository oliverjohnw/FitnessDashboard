from django.contrib import admin
from .models import LiftPost, LiftPostSet, YogaPost, YogaPose
from .models import RunningPost, BikingPost, HiitPost, WalkingPost

# Register your models here.
class ExerciseInline(admin.TabularInline):
    model = LiftPostSet
    extra = 1  # Number of empty forms to display for adding new WorkoutSet instances

@admin.register(LiftPost)
class WorkoutAdmin(admin.ModelAdmin):
    inlines = [ExerciseInline]

admin.site.register(YogaPost)
admin.site.register(RunningPost)
admin.site.register(BikingPost)
admin.site.register(WalkingPost)
admin.site.register(HiitPost)