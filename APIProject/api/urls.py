from django.urls import path, include
# from .views import artile_list, article_details
# from .views import ArticleList, ArticleDetails
from .views import ArticleViewset, UserViewset
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('articles', ArticleViewset, basename='articles')
router.register('users', UserViewset)

urlpatterns = [
    path('api/', include(router.urls))

    #  path('article/', ArticleList.as_view()),
    #  path('article/<int:id>/', ArticleDetails.as_view())


    # path('article/', artile_list),
    # path('article/<int:pk>/', article_details),

    
]
