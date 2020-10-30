  
from rest_framework import routers

from .api import Taskviewset

router=routers.DefaultRouter()
router.register("api/tasks",Taskviewset,"tasks")

urlpatterns=router.urls