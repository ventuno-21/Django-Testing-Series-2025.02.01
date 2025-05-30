"""
URL configuration for A_config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("app_test1.urls")),
    path("account/", include("app_account.urls")),
    path("products/", include("app_products.urls")),
    path("api-auth/", include("rest_framework.urls")),
    path("api/", include("app_pytest.urls")),
    path("blog/", include("app_blog.urls")),
]

# if settings.DEBUG:
# 	urlpatterns += static(settings.MEDIA_URL,
# 						  document_root=settings.MEDIA_ROOT)
