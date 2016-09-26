from django.conf.urls import url
from . import views

urlpatterns = [
	url(r"^$", views.index, name="index"),
	url(r"^create_poke/(?P<pokee_id>\d+)$", views.create_poke, name="create_poke")
]
