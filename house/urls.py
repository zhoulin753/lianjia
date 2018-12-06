from django.conf.urls import url
from house import views
urlpatterns = [
    url(r'^index/',views.index)



]