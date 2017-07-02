from .api import ListViewSet, CardViewSet, UsersViewsSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'lists', ListViewSet, base_name='lists')
router.register(r'cards', CardViewSet)
router.register(r'users', UsersViewsSet)

urlpatterns = router.urls
