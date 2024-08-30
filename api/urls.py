from rest_framework.routers import DefaultRouter
from .views import NoteViewSet, TaskViewSet, FileViewSet

router = DefaultRouter()
router.register(r'notes', NoteViewSet, basename='note')
router.register(r'tasks', TaskViewSet, basename='task')
router.register(r'files', FileViewSet, basename='file')

urlpatterns = router.urls
