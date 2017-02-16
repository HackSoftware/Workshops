from django.conf.urls import url

from .views import UniversalTruth


urlpatterns = [
    url(r'truth/$', UniversalTruth.as_view(), name='truth')
]
