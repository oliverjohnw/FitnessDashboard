from django.shortcuts import render
from .models import LiftPost, LiftPostSet, YogaPost, YogaPose
from .models import RunningPost, BikingPost, HiitPost, WalkingPost
from django.http import JsonResponse

def post_list_and_create(request):
    qs = LiftPost.objects.all()
    return render(request, 'workout_posts/main.html', {'qs':qs})

# Create your views here.
def load_all_workout_posts(request, num_posts):
    visible = 3
    upper = num_posts
    lower = upper - visible\
    
    # data
    lift_posts = LiftPost.objects.all()
    yoga_posts = YogaPost.objects.all()
    running_posts = RunningPost.objects.all()
    biking_posts = BikingPost.objects.all()
    hiit_posts = HiitPost.objects.all()
    walking_posts = WalkingPost.objects.all()

    lift_data = []
    yoga_data = []
    running_data = []
    biking_data = []
    hiit_data = []
    walking_data = []

    # lifting
    for obj in lift_posts:
        sets = LiftPostSet.objects.filter(workout=obj)
        sets_data = []

        for set_obj in sets:
            set_item = {
                'workout_name': set_obj.workout_name,
                'reps': set_obj.reps,
                'weight': set_obj.weight,
                'duration': set_obj.duration,
                'notes': set_obj.notes
            }
            sets_data.append(set_item)

        item = {
            'exercise': obj.exercise_string,
            'body_part': obj.body_part,
            'date': obj.date,
            'time_of_day': obj.time_of_day,
            'duration': obj.duration,
            'location': obj.location,
            'mood_before': obj.mood_before,
            'mood_after': obj.mood_after,
            'notes': obj.notes,
            'includes_abs': obj.includes_abs,
            'sets': sets_data
        }
        lift_data.append(item)

    # yoga
    for obj in yoga_posts:
        poses = YogaPose.objects.filter(session=obj)
        poses_data = []

        for pose_obj in poses:
            pose_item = {
                'pose_name': pose_obj.pose_name,
                'duration': pose_obj.duration
            }
            poses_data.append(pose_item)

        item = {
            'exercise': obj.exercise_string,
            'yoga_type': obj.yoga_type,
            'date': obj.date,
            'time_of_day': obj.time_of_day,
            'duration': obj.duration,
            'location': obj.location,
            'mood_before': obj.mood_before,
            'mood_after': obj.mood_after,
            'notes': obj.notes,
            'instructor': obj.instructor,
            'poses': poses_data
        }
        yoga_data.append(item)

    # running
    for obj in running_posts:
        item = {
            'exercise': obj.exercise_string,
            'date': obj.date,
            'time_of_day': obj.time_of_day,
            'distance_miles': obj.distance_miles,
            'duration': obj.duration,
            'location': obj.location,
            'temperature': obj.location,
            'weather_conditions': obj.weather_conditions,
            'terrain': obj.terrain,
            'mood_before': obj.mood_before,
            'mood_after': obj.mood_after,
            'notes': obj.notes
        }
        running_data.append(item)

    # biking
    for obj in biking_posts:
        item = {
            'exercise': obj.exercise_string,
            'date': obj.date,
            'time_of_day': obj.time_of_day,
            'distance_miles': obj.distance_miles,
            'duration': obj.duration,
            'location': obj.location,
            'temperature': obj.location,
            'weather_conditions': obj.weather_conditions,
            'terrain': obj.terrain,
            'mood_before': obj.mood_before,
            'mood_after': obj.mood_after,
            'notes': obj.notes
        }
        biking_data.append(item)

    # walking
    for obj in walking_posts:
        item = {
            'exercise': obj.exercise_string,
            'date': obj.date,
            'time_of_day': obj.time_of_day,
            'duration': obj.duration,
            'location': obj.location,
            'temperature': obj.location,
            'weather_conditions': obj.weather_conditions,
            'terrain': obj.terrain,
            'mood_before': obj.mood_before,
            'mood_after': obj.mood_after,
            'notes': obj.notes
        }
        walking_data.append(item)

    # hiit
    for obj in hiit_posts:
        item = {
            'exercise': obj.exercise_string,
            'title': obj.exercise_label,
            'date': obj.date,
            'time_of_day': obj.time_of_day,
            'duration': obj.duration,
            'location': obj.location,
            'mood_before': obj.mood_before,
            'mood_after': obj.mood_after,
            'notes': obj.notes
        }
        hiit_data.append(item)
    
    all_data = lift_data + yoga_data + running_data + biking_data + walking_data + hiit_data
    size = len(all_data)
    
    return JsonResponse({'workout_data': all_data[lower:upper],
                         'size': size})

