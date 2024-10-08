from django.conf import settings
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.status import (HTTP_404_NOT_FOUND,
                                   HTTP_400_BAD_REQUEST, HTTP_200_OK,
                                   HTTP_201_CREATED, HTTP_403_FORBIDDEN, HTTP_204_NO_CONTENT)
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, IsAdminUser

from ..serializers.task_serializers import TaskOneSerializer
from ..services.cache_service import delete_cache_by_pattern, delete_cache_by_key, get_cache, set_cache
from ..services.course_service import get_course_by_id
from ..services.task_service import create_task, update_task, delete_task, add_remove_task_experience, \
    add_remove_task_bookmark, get_task_by_id, update_tasks_places
from ..services.title_service import get_course_title_by_id


@api_view(['POST'])
@permission_classes([IsAdminUser])
def task_create(request, course_id: int, title_id: int):
    """
        Создание задания
    """
    # Берем курс по идентификатору
    course = get_course_by_id(course_id)
    if not course:
        return Response({'detail': f'Course with ID: {course_id} not found.'}, status=HTTP_404_NOT_FOUND)

    # Берем тему задания к курсу по его идентификатору
    course_title = get_course_title_by_id(title_id)
    if not course_title:
        return Response({'detail': f'Title with ID: {title_id} not found.'}, status=HTTP_404_NOT_FOUND)

    # Берем данные
    title = request.data.get('title', '')
    task_type = request.data.get('type', 'text')
    points = request.data.get('points', 0)

    # Создаем таск
    task = create_task(course_title, title, task_type, points)

    # Проверяем, что таск создан успешно и выводи сообщение
    if task:
        # Удаляем весь кэш для пользователей
        delete_cache_by_pattern(f'course_titles_and_tasks_list_history_{course_id}')
        return Response({'detail': 'The subject created successfully!'}, status=HTTP_201_CREATED)
    return Response({'detail': 'Task creation failed'}, status=HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def task_get_update_delete(request, course_id: int, task_id: int):
    """
        Вывод, обновление и удаление задания
    """
    # Берем курс по его идентификатору
    course = get_course_by_id(course_id)
    if not course:
        return Response({'detail': f'Course with ID: {course_id} not found.'}, status=HTTP_404_NOT_FOUND)

    # Генерируем ключ для кэша на основе параметров запроса
    cache_key_patten = f"course_task_history_{task_id}"

    if request.method == 'GET':
        cache_key = f'{cache_key_patten}_{request.user.username}'
        # Берем данные из кэша
        cache_data = get_cache(cache_key)
        if cache_data:
            return Response(cache_data, status=HTTP_200_OK)

        # Берем задание по его идентификатору
        task = get_task_by_id(task_id)
        if not task:
            return Response({'detail': f'Task with ID: {task_id} not found.'}, status=HTTP_404_NOT_FOUND)

        serializer = TaskOneSerializer(task, many=False, context={'user': request.user})
        # Кешируем данные
        set_cache(cache_key, serializer.data, timeout=settings.COURSE_TITLE_AND_TASK_LIST_CACHE_TIMEOUT)
        return JsonResponse(serializer.data, status=200)

    # Берем задание по его идентификатору
    task = get_task_by_id(task_id)
    if not task:
        return Response({'detail': f'Task with ID: {task_id} not found.'}, status=HTTP_404_NOT_FOUND)

    if not request.user.is_superuser:
        return Response({'detail': 'User does not have sufficient rights'}, status=HTTP_403_FORBIDDEN)

    elif request.method == 'PUT':
            # Берем данные
            title = request.data.get('task_title', '')
            public = request.data.get('public', 'false')
            points = request.data.get('points', 0)

            # Обновляем задание
            if update_task(task, title, public, points):
                # Удаляем весь кэш для пользователей
                delete_cache_by_pattern('course_titles_and_tasks_list_history')
                delete_cache_by_pattern(cache_key_patten)
                return Response({'detail': 'Task updated successfully!'}, status=HTTP_200_OK)
            return Response({'detail': 'Task updation failed'}, status=HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        # Удаляем задание
        delete_task(task)
        # Удаляем весь кэш для пользователей
        delete_cache_by_pattern(f'course_titles_and_tasks_list_history_{course_id}')
        delete_cache_by_pattern(cache_key_patten)
        return Response({}, status=HTTP_204_NO_CONTENT)


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def task_add_experience(request, course_id: int, task_id: int):
    """
        Добавление / удаление опыта
    """
    # Берем курс по его идентификатору
    course = get_course_by_id(course_id)
    if not course:
        return Response({'detail': f'Course with ID: {course_id} not found.'}, status=HTTP_404_NOT_FOUND)

    # Берем задание по его идентификатору
    task = get_task_by_id(task_id)
    if not task:
        return Response({'detail': f'Task with ID: {task_id} not found.'}, status=HTTP_404_NOT_FOUND)

    # Добавляем или удаляем опыт к заданию
    message = add_remove_task_experience(task, request.user)
    # Удаляем весь кэш для текущего пользователя
    delete_cache_by_key(f'course_titles_and_tasks_list_history_{course_id}_{request.user.username}')
    delete_cache_by_key(f'course_task_history_{task_id}_{request.user.username}')
    return Response({'detail': message}, status=HTTP_200_OK)


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def task_add_remove_bookmark(request, course_id: int, task_id: int):
    """
        Добавление / удаление из закладок
    """
    # Берем курс по его идентификатору
    course = get_course_by_id(course_id)
    if not course:
        return Response({'detail': f'Course with ID: {course_id} not found.'}, status=HTTP_404_NOT_FOUND)

    # Берем задание по его идентификатору
    task = get_task_by_id(task_id)
    if not task:
        return Response({'detail': f'Task with ID: {task_id} not found.'}, status=HTTP_404_NOT_FOUND)

    # Добавляем или удаляем закладку к заданию
    message = add_remove_task_bookmark(task, request.user)
    # Удаляем весь кэш для текущего пользователя
    delete_cache_by_key(f'course_titles_and_tasks_list_history_{course_id}_{request.user.username}')
    delete_cache_by_key(f'course_task_history_{task_id}_{request.user.username}')
    return Response({'detail': message}, status=HTTP_200_OK)


@api_view(['PATCH'])
@permission_classes([IsAdminUser])
def task_change_titles_tasks_places(request, course_id: int, task1_id: int, task2_id: int):
    """
        Смена тем местами
    """
    # Берем курс по идентификатору
    course = get_course_by_id(course_id)
    if not course:
        return Response({'detail': f'Course with ID: {course_id} not found.'}, status=HTTP_404_NOT_FOUND)

    # Берем первое задание по его идентификатору
    task1 = get_task_by_id(task1_id)
    if not task1:
        return Response({'detail': f'Task with ID: {task1_id} not found.'}, status=HTTP_404_NOT_FOUND)

    # Берем второе задание по его идентификатору
    task2 = get_task_by_id(task2_id)
    if not task2:
        return Response({'detail': f'Task with ID: {task2_id} not found.'}, status=HTTP_404_NOT_FOUND)

    # Обновляем данные
    if update_tasks_places(task1, task2):
        # Удаляем весь кэш для пользователей
        delete_cache_by_pattern(f'course_titles_and_tasks_list_history_{course_id}')
        return Response({'detail': 'Task\'s order changed successfully!'}, status=HTTP_200_OK)
    return Response({'detail': 'Task\'s order changed failed'}, status=HTTP_400_BAD_REQUEST)

