from django.urls import path
from .views import (
    post_list_and_create,
    load_all_workout_posts,
)

app_name = 'workout_posts'

urlpatterns = [
    path('', post_list_and_create, name='main-board'),
    path('data/<int:num_posts>/', load_all_workout_posts, name = 'posts-data'),
]