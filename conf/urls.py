from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView
from rest_framework import permissions

schema = SpectacularSwaggerView(permission_classes=(permissions.AllowAny,))

urlpatterns = [
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', schema.as_view(url_name='schema'), name='docs'),
    path('admin/', admin.site.urls),
    # third
    path('api/v1/', include('api.v1.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
