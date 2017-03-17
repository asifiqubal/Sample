
from django.conf.urls import url
from . import views

app_name = 'student'
urlpatterns = [
    # /student/
    url(r'^$', views.index, name='index'),
    # /student/<sid>/
    url(r'^student/(?P<sid>[0-9][0-9]-[0-9][0-9][0-9][0-9][0-9]-[1-3])$', views.student, name='student'),
]
