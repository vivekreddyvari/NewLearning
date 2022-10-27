from django.urls.conf import include, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView, DetailsView
from rest_framework .authtoken.views import obtain_auth_token
from django.views.generic.base import TemplateView

urlpatterns = [
    re_path("accounts/", include('django.contrib.auth.urls')),
    # re_path('', TemplateView.as_view(template_name='home.html'), name='home'),
    re_path(r'^auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    re_path(r'^blogposts/$', CreateView.as_view(), name='create'),
    re_path(r'^blogposts/(?P<pk>[0-9]+)/$',
            DetailsView.as_view(), name="details"),
    re_path(r'^get-token/', obtain_auth_token),
]
urlpatterns = format_suffix_patterns(urlpatterns)
