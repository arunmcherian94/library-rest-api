from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from crud import views
 
urlpatterns = [
    url(r'^member/$', views.MemberOperations.as_view(), name='member_route'),
    url(r'^book/$', views.BookOperations.as_view(), name='book_route'),
    url(r'^actions/$', views.BookActions.as_view(), name='book_action_route'),
]