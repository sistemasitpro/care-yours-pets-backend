# rest framework
from rest_framework import routers

# views
from .views import Veternary


router = routers.SimpleRouter()
router.register(r'veterinaries', Veternary, basename='veterinary-info')

urlpatterns = router.urls