from django.conf.urls import url
from . import views

# namespace
app_name = 'music'

"""
urlpatterns = [
	# /music/
    url(r'^$', views.index, name='index'),

    # /music/<album_id>/
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name="detail"),

    # /music/<album_id>/favorite
    url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name="favorite"),
]
"""

urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name="detail"),

	# /music/album/add/
	url(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),	
]
