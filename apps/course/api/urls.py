from django.urls import path
from .views import courses, tags, titles, tasks, task_comment

app_name = 'course'

urlpatterns = [
    # TODO: Tags
    path('tags/', tags.tag_create_list, name='tags_list_create'),
    path('tags/<int:id>/', tags.tags_get_update_delete, name='tags_get_update_delete'),

    # TODO: Courses
    path('courses/', courses.courses_list, name='courses_list_create'),
    path('courses/<int:id>/', courses.courses_get, name='courses_get_update_delete'),
    path('courses/<int:id>/like/', courses.course_add_remove_like, name='course_add_remove_like'),
    path('courses/<int:id>/user/', courses.course_add_remove_user, name='course_add_remove_user'),
    path('courses/<int:id>/reviews/', courses.course_review_create_list, name='course_review_create_list'),
    path('courses/reviews/<int:id>/delete/', courses.course_reviews_delete, name='course_reviews_delete'),

    # TODO: Title
    path('courses/<int:id>/titles/',
         titles.title_list_create, name='title-list-create'),
    path('courses/titles/<int:title_id>/',
         titles.title_delete, name='title-delete'),
    path('courses/titles/<int:title_id>/update-title/',
         titles.title_update_name, name='title-update-name'),
    path('courses/titles/<int:title_id>/update-public/',
         titles.title_update_public, name='title-update-public'),
    # path('courses/<int:id>/titles/<int:TitleID>/places/<int:NewOrder>/',
    #      titles.title_change_place, name='title-change-place'),

    # TODO: TASK
    path('courses/titles/<int:id>/tasks/',
         tasks.task_create, name='task-create'),
    path('courses/<int:id>/titles/tasks/<int:task_id>/',
         tasks.task_get_update_delete, name='task-update-delete'),
    path('courses/<int:id>/titles/tasks/<int:task_id>/experience/',
         tasks.task_add_experience, name='task_add_experiense'),
    path('courses/<int:course_id>/titles/tasks/<int:task_id>/bookmark/',
         tasks.task_add_remove_bookmark, name='task_add_remove_bookmark'),

    # TODO: TASK COMMENTS
    path('courses/titles/tasks/<int:task_id>/comments/',
         task_comment.task_comment_list_create, name='task_comment_list_create'),
    path('courses/titles/tasks/<int:task_id>/comments/<int:comment_id>/delete/',
         task_comment.task_comment_delete, name='task_comment_delete'),
    path('courses/titles/tasks/<int:task_id>/comments/<int:comment_id>/react/',
         task_comment.task_comment_add_remove_like, name='task_comment_add_remove_like'),
    path('courses/titles/tasks/<int:task_id>/comments/<int:comment_id>/complaint/',
         task_comment.task_comment_add_complaint, name='task_comment_add_complaint')
]
