from django.contrib import admin
from django.urls import path

# from rest_framework_jwt.views import obtain_jwt_token
from django.conf.urls.static import static
from django.conf import settings
from api.views import (
	UserCreateAPIView,
	UserLoginAPIView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', UserCreateAPIView.as_view(), name="signup"),
    path('signin/',UserLoginAPIView.as_view(), name="signin"),
]


urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)