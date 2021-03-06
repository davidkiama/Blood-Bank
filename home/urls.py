from django.urls import path
from . import views


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('hos/signup', views.hos_signup, name='hos_signup'),
    path('hos/login', views.hos_login, name='hos_login'),
    path('hos/blood_drive', views.hos_create_blood_drive,
         name='hos_create_blood_drive'),

    path('hos/list_of_donors', views.list_of_donors, name='donors_list'),
    path('hos/dashboard', views.hos_dashboard, name="hos_dashboard"),


    path('don/signup', views.don_signup, name="don_signup"),
    path('don/login', views.don_login, name="don_login"),
    path('don/donate', views.don_apply_to_donate, name='don_donate'),

    path("logout", views.logout_request, name="logout"),
    path('active_campaigns', views.active_campaigns, name='active_campaigns')


]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
