from django.urls import path
from originsite.views.views import SampleDataListCreateAPIView
from originsite.views.api_views import SampleDataListAPIView
from originsite.views.post_views import SampleDataPostListAPIView
from rest_framework import routers
from originsite import views
# from api import views as api_views

# 登録用API
router = routers.DefaultRouter()
router.register("sample_create", SampleDataListCreateAPIView, "list")

# API
urlpatterns = [
    path("sample_list/", SampleDataListAPIView.as_view()),
    path("sample_response/", SampleDataPostListAPIView.as_view()),
]
