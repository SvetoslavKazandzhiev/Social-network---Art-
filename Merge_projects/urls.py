from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from authy.views import UserProfile, follow
from post_art.views import IndexView

urlpatterns = [
                  path('', IndexView.as_view(), name='landing'),
                  path('', LoginView.as_view(template_name='login.html'), name='login'),
                  path('admin/', admin.site.urls),
                  path('post/', include('post_art.urls')),
                  path('user/', include('authy.urls')),
                  path('direct/', include('direct.urls')),
                  path('stories/', include('stories.urls')),
                  path('notifications/', include('notifications.urls')),
                  path('<username>/', UserProfile, name='profile'),
                  path('<username>/saved', UserProfile, name='profilefavorites'),
                  path('<username>/follow/<option>', follow, name='follow'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
