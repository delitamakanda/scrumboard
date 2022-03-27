from .api import ListViewSet, CardViewSet, UsersViewsSet, TodoViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'lists', ListViewSet, basename='lists')
router.register(r'cards', CardViewSet, basename='cards')
router.register(r'users', UsersViewsSet, basename='users')
router.register(r'todos', TodoViewSet, basename='todos')

urlpatterns = router.urls
