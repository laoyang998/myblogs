from django.urls import path
from django.views.generic import TemplateView
from .views import AboutView, CourseListView, ManageCourseListView,CreateCourseView,DeleteCourseView,\
    CreateLessonView,ListLessonView,DetailLessonView,StudentListLessonView


app_name = 'course'
urlpatterns = [
    # path('about', TemplateView.as_view(template_name='course/about.html'), name='about'),
    path('about', AboutView.as_view(), name='about'),
    path('course_list', CourseListView.as_view(), name='course_list'),
    path('manage_course', ManageCourseListView.as_view(), name='manage_course'),
    path('create_course', CreateCourseView.as_view(), name='create_course'),
    path('delete_course/<pk>', DeleteCourseView.as_view(), name='delete_course'),
    path('create_lesson', CreateLessonView.as_view(), name='create_lesson'),
    path('list_lesson/<course_id>', ListLessonView.as_view(), name='list_lesson'),
    path('detail_lesson/<lesson_id>', DetailLessonView.as_view(), name='detail_lesson'),
    path('lesson_slist/<course_id>', StudentListLessonView.as_view(), name='lesson_slist'),
]
