# rest framework
from rest_framework import routers

# views
from .views import Veterinary


router = routers.SimpleRouter()
router.register(r'veterinaries', Veterinary, basename='veterinary-info')

urlpatterns = router.urls