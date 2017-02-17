from django.conf.urls import url

from rest_framework_jwt.views import obtain_jwt_token

from .views import UniversalTruth


urlpatterns = [
    url(r'^jwt-login/$', obtain_jwt_token),
    url(r'truth/$', UniversalTruth.as_view(), name='truth')
]
