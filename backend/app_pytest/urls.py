from rest_framework import routers
from .views import CompanyViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
#     TokenVerifyView,
# )

app_name = "app_pytest"
# Create a router and register our ViewSets with it.
companies_router = routers.DefaultRouter()
companies_router.register("companies", viewset=CompanyViewSet, basename="companies")

urlpatterns = [
    path("", include(companies_router.urls)),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    # Optional UI:
    path(
        "swagger/",
        SpectacularSwaggerView.as_view(url_name="app_pytest:schema"),
        name="swagger-ui",
    ),
    path(
        "redoc/",
        SpectacularRedocView.as_view(url_name="app_pytest:schema"),
        name="redoc",
    ),
    #     path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    #     path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    #     path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
]
