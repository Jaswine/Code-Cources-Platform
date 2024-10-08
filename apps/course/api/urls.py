from django.urls import path

from .views import courses, tags, titles, tasks, task_comment

app_name = 'course'

urlpatterns = [
    path('tags/', tags.tag_create_list, name='tags_list_create'),
    path('tags/<int:id>/', tags.tags_get_update_delete, name='tags_get_update_delete'),

    path('', courses.courses_list_create, name='courses_list_create'),
    path('<int:id>/', courses.courses_show_delete, name='courses_get_update_delete'),
    path('<int:id>/like/', courses.course_add_remove_like, name='course_add_remove_like'),
    path('<int:id>/user/', courses.course_add_remove_user, name='course_add_remove_user'),
    path('<int:course_id>/reviews/', courses.course_review_create_list, name='course_review_create_list'),
    path('<int:course_id>/reviews/<int:review_id>/delete/', courses.course_reviews_delete, name='course_reviews_delete'),

    path('<int:course_id>/titles/',
         titles.title_list_create, name='title-list-create'),
    path('<int:course_id>/titles/<int:title_id>/',
         titles.title_delete, name='title-delete'),
    path('<int:course_id>/titles/<int:title_id>/update-title/',
         titles.title_update_name, name='title-update-name'),
    path('<int:course_id>/titles/<int:title_id>/update-public/',
         titles.title_update_public, name='title-update-public'),
    path('<int:course_id>/titles/<int:title1_id>/change-place/<int:title2_id>/',
         titles.title_change_titles_place, name='title-change-titles-place'),

    path('<int:course_id>/titles/<int:title_id>/tasks/',
         tasks.task_create, name='task-create'),
    path('<int:course_id>/titles/tasks/<int:task_id>/',
         tasks.task_get_update_delete, name='task-update-delete'),
    path('<int:course_id>/titles/tasks/<int:task_id>/experience/',
         tasks.task_add_experience, name='task_add_experience'),
    path('<int:course_id>/titles/tasks/<int:task_id>/bookmark/',
         tasks.task_add_remove_bookmark, name='task_add_remove_bookmark'),
    path('<int:course_id>/titles/tasks/<int:task1_id>/change-place/<int:task2_id>/',
         tasks.task_change_titles_tasks_places, name='task_change_titles_tasks_places'),

    path('titles/tasks/<int:task_id>/comments/',
         task_comment.task_comment_list_create, name='task_comment_list_create'),
    path('titles/tasks/<int:task_id>/comments/<int:comment_id>/',
         task_comment.task_comment_delete, name='task_comment_delete'),
    path('titles/tasks/<int:task_id>/comments/<int:comment_id>/react/',
         task_comment.task_comment_add_remove_like, name='task_comment_add_remove_like'),
    path('titles/tasks/<int:task_id>/comments/<int:comment_id>/complaint/',
         task_comment.task_comment_add_complaint, name='task_comment_add_complaint')
]
