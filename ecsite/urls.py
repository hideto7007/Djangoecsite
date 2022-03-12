from django.urls import path
from ecsite.views.views import SampleDataListCreateAPIView
from ecsite.views.api_views import SampleDataListAPIView
from ecsite.views.post_views import SampleDataPostListAPIView
from rest_framework import routers
from ecsite import views
# from api import views as api_views

# 登録用API
router = routers.DefaultRouter()
router.register("sample_create", SampleDataListCreateAPIView, "list")

# API
urlpatterns = [
    path("sample_list/", SampleDataListAPIView.as_view()),
    path("sample_response/", SampleDataPostListAPIView.as_view()),
]
