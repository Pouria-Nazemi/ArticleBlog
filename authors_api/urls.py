from django.urls import include, path
from rest_framework import routers
from authors_api import views


router = routers.DefaultRouter()
router.register('Authors',views.AuthorViewset)

urlpatterns = [
    path('', include(router.urls))
]