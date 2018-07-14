from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^componentdashboard/$', views.ComponentDashboard.as_view()),
    url(r'^machinedashboard/$', views.MachineDashboard.as_view()),
    url(r'^dashboard/$', views.Dashboard.as_view()),
    url(r'^list/$', views.List.as_view()),
    url(r'^addcomponent/$', views.AddComponent.as_view()),
    url(r'^assignmentdashboard/$', views.AssignmentDashboard.as_view()),
    url(r'^login/$', views.UserLogin.as_view()),
    url(r'^sensordata/$', views.SensorData.as_view())

]
