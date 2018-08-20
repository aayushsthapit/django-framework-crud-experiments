from rest_framework.routers import DefaultRouter
from views import ListTableData
from django.conf.urls import url,include
router=DefaultRouter()
router.register('todos',ListTableData)


urlpatterns = [
    url(r'^', include(router.urls)),

]