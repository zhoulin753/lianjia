from django.conf.urls import url
from house import views
urlpatterns = [
    url(r'^index/',views.index),
    url(r'pg(\d+)', views.get_page)


]