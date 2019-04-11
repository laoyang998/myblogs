from django.urls import path
from django.views.generic import TemplateView
from .views import AboutView, CourseListView, ManageCourseListView,CreateCourseView

app_name = 'course'
urlpatterns = [
    # path('about', TemplateView.as_view(template_name='course/about.html'), name='about'),
    path('about', AboutView.as_view(), name='about'),
    path('course_list', CourseListView.as_view(), name='course_list'),
    path('manage_course', ManageCourseListView.as_view(), name='manage_course'),
    path('create_course', CreateCourseView.as_view(), name='create_course'),
]
