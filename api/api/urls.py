from django.urls import include, path
from rest_framework_swagger.views import get_swagger_view
from rest_framework import routers
from api import views
from backend import settings

router = routers.DefaultRouter()
router.register(r"offer", views.OfferViewSet)
schema_view = get_swagger_view(title="Job offers")

app_name = "api"
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [path("", include(router.urls))]

if settings.DEBUG:
    urlpatterns += [path("docs/", schema_view)]
