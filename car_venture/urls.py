from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("brand/<slug:brand_slug>/", views.home, name="brand_wise"),
    path("register/", views.UserRegisterView.as_view(), name="register"),
    path("login/", views.UserLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("profile/", views.UserProfileView.as_view(), name="profile"),
    path("update-profile/", views.updateProfile, name="update-profile"),
    path(
        "change-password/", views.UserChangePassword.as_view(), name="change-password"
    ),
    path("car/", include("car.urls")),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
