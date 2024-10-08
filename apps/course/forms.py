from django.forms import ModelForm, CheckboxSelectMultiple
from .models import Course, Tag, Task, TaskCommentUserComplaint


class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = [
            'title', 'image',
            'tags', 'about', 'public',
        ]
        widgets = {
            'tags': CheckboxSelectMultiple,
        }


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = [
            'title',
            'text',
        ]


class TaskCommentUserComplaintForm(ModelForm):
    class Meta:
        model = TaskCommentUserComplaint
        fields = ['type', 'message']
