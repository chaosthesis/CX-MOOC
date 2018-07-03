from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

class CourseApp(CMSApp):
    name = _("course")
    urls = ["CXMOOC_Course.urls"]

apphook_pool.register(CourseApp)