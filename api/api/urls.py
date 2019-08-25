from api import views

from backend import settings

from django.urls import include, path

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from rest_framework import permissions, routers

router = routers.DefaultRouter()
router.register(r"example", views.ExampleViewSet)
schema_view = get_schema_view(
    openapi.Info(
        title="Example API",
        default_version="v1",
        description="API description",
        contact=openapi.Contact(email="jdesmare@student.42.fr"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

app_name = "api"
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [path("", include(router.urls))]

if settings.DEBUG:
    urlpatterns += [
        path(
            "swagger/",
            schema_view.with_ui("swagger", cache_timeout=0),
            name="schema-swagger-ui",
        ),
        path(
            "redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
        ),
    ]
