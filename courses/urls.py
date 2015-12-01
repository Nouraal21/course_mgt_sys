from django.conf.urls import url
from courses import views

urlpatterns = [
    url(r'^course/create/$', views.course_create,
        name='course_create'),
    url(r'^course/grade/$', views.CourseGradeView.as_view(),
        name='course_grade'),
    url(r'^course/(?P<course_id>\d+)/enroll/(?P<student_id>\d+)',
        views.enroll_student_to_course, name='enroll'),
    url(r'^course/(?P<pk>\d+)/edit/$', views.CourseEdit.as_view(),
        name='course_edit',),

]
