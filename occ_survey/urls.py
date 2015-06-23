from django.conf.urls import include, url
from occ_survey import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^survey/(?P<survey_name>[\w\-]+)/$', views.survey, name="survey"),
    url(r'^submit_profile/$', views.submit_profile, name="submit_profile"),
    url(r'^chart_daily_consumption/$', views.chart_daily_consumption, name="chart_cons")
]