from apps.account import views
from rest_framework import routers

router = routers.SimpleRouter()

router.register(r'api/account', views.AccountViewSet, base_name='account')
router.register(r'api/keys', views.AccessApiKeyViewSet, base_name='keys')

urlpatterns = router.urls
