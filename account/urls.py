from django.conf.urls import url
from django.conf.urls import url

from account import views

urlpatterns = [
    url(
        r'^register/$',
        views.register,
        name='register'
    ),
    url(
        r'^register-auth/$',
        views.register_authenticated,
        name='register-authenticated'
    ),
    url(
        r'^register/(?P<activation_key>\w+)/$',
        views.register_invited,
        name='register-invite'
    ),
    url(
        r'^register-premium-auth/(?P<activation_key>[\w]+)/$',
        views.register_premium_auth,
        name='register-premium-auth'
    ),
    url(
        r'^register-premium/(?P<activation_key>[\w]+)/$',
        views.register_premium,
        name='register-premium'
    ),
    url(
        r'^activate/(?P<activation_key>\w+)/$',
        views.activate,
        name='activate'
    ),
    url(
        r'^logout/$',
        views.logout_view,
        name='logout'
    ),
    url(
        r'^dashboard/$',
        views.dashboard,
        name='dashboard'
    ),
    url(
        r'^profile/$',
        views.view_profile,
        name='view-profile'
    ),
    url(
        r'^profile/edit/$',
        views.edit_profile,
        name='edit-profile'
    ),
    url(
        r'^invite/$',
        views.send_invite,
        name='send-invite'
    ),
    url(
        r'^invite/revoke/(?P<invite_id>\d+)/$',
        views.revoke_invite,
        name='revoke-invite'
    ),
    url(
        r'^revoke/(?P<user_id>\d+)/$',
        views.revoke_access,
        name='revoke-access'
    ),
    url(
        r'accept/(?P<activation_key>\w+)/$',
        views.accept_invite,
        name='accept-invite'
    )    
    
]
