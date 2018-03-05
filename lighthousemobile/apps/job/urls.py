from rest_framework import routers
from . import views

router = routers.SimpleRouter(trailing_slash=False)

router.register(r'api/job/form', views.JobFormViewSet, base_name='form')

urlpatterns = router.urls
