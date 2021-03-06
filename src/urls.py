from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'', include('pages.urls', namespace='pages')),
    # url(r'', include('datasets.urls', namespace='datasets')),
    # url(r'^participants/', include('participants.urls', namespace='participants')),
    url(r'^submissions/', include('submissions.urls', namespace='submissions')),
    # url(r'', include('workers.urls', namespace='workers')),

    url(r'^s3direct/', include('s3direct.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
