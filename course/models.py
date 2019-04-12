from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from slugify import slugify


class Course(models.Model):
    user = models.ForeignKey(User, related_name='course_user', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=300, unique=True)
    student = models.ManyToManyField(User, related_name='courses_joined', blank=True)
    overview = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Course, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


def user_derictory_path(instance, filename):
    return 'course/user_{0}/{1}'.format(instance.user.id, filename)


class OrderField(models.PositiveIntegerField):
    def __init__(self, for_fields=None, *args, **kwargs):
        self.for_fields = for_fields
        super(OrderField, self).__init__(*args, **kwargs)

    def pre_save(self, model_instance, add):
        if getattr(model_instance, self.attname) is None:
            try:
                qs = self.model.objects.all()
                if self.for_fields:
                    query = {field: getattr(model_instance, field) for field in self.for_fields}
                    qs = qs.filter(**query)
                    last_item = qs.latest(self.attname)
                    value = last_item.order + 1
            except ObjectDoesNotExist:
                value = 0
            setattr(model_instance, self.attname, value)
            return value


class Lesson(models.Model):
    user = models.ForeignKey(User, related_name='lesson_user', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name='lesson', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    video = models.FileField(upload_to=user_derictory_path)
    description = models.TextField()
    attach = models.FileField(blank=True, upload_to=user_derictory_path)
    order = OrderField(blank=True, for_fields=['course'])
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return '{}.{}'.format(self.order, self.title)
