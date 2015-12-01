from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, UpdateView
from django.contrib import messages

from .forms import NewCourseForm
from .models import GradeColumn

from students.models import Student
from courses.models import Course
# Create your views here.


def course_create(request):
    if request.method == 'POST':
        form = NewCourseForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            return redirect()
    else:
        form = NewCourseForm()
    return render(
        request,
        'course_create.html',
        {
            "form": form,
        }
    )


# def course_edit(request, course_id):
#     course = get_object_or_404(Course, pk=course_id)
#     if request.method == 'POST':
#         form = NewCourseForm(request.POST, instance=course)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'course was successfully edited.')
#             return redirect('/')
#     else:
#         form = NewCourseForm(instance=course)
#     return render(
#         request,
#         'course_edit.html',
#         {
#             "course": course,
#             "form": form,
#         }
#     )


class CourseEdit(UpdateView):
    model = Course
    template_name = "course_edit.html"
    context_object_name = "form"
    fields = '__all__'

class CourseGradeView(ListView):
    model = GradeColumn
    template_name = "course_grade.html"


def enroll_student_to_course(request, course_id, student_id):
    course = Course.objects.get(pk=course_id)
    student = Student.objects.get(pk=student_id)
    course.students.add(student)
    course.save()
    messages.success(request, 'The student is successfuly added.')
    return redirect('/')
