from rest_framework.routers import DefaultRouter
import board.views
router=DefaultRouter()
router.register(r'sprsints',board.views.SprintViewSet,)
router.register(r'tasks',board.views.TaskViewSet,)
router.register(r'users',board.views.UserViewSet,)
