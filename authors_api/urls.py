from django.urls import include, path
from rest_framework import routers
from authors_api import views


router = routers.DefaultRouter()
router.register('Authors',views.AuthorViewset)
router.register('Articles',views.ArticleViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', views.UserLoginApiView.as_view()),

]