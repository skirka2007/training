from django.conf.urls import url
from qa.views import question_page

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', question_page),
]

