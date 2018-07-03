from django.conf.urls import patterns, url

from CXMOOC_Course import views

urlpatterns = patterns('',
    url(r'^$','CXMOOC_Course.views.search_course', name='search'),
    url(r'^course_content/',views.coursedev_view),
)