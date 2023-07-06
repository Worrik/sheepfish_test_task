from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r"checks", views.CheckViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("print/", views.PrintView.as_view()),
]
