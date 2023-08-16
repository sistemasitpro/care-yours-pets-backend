# rest framework
from rest_framework import routers

# views
from .views import Veternary


router = routers.SimpleRouter()
router.register(r'veterinary', Veternary, basename='veterinary-info')

urlpatterns = router.urls