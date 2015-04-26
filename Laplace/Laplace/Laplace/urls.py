from django.conf.urls import include, url
from django.contrib import admin
from rest_framework_nested import routers
from User.views import UserViewSet
from Post.views import UserPostViewSet, PostViewSet


router = routers.SimpleRouter()
router.register(r'users', UserViewSet)
router.register(r'posts', PostViewSet)
accounts_router = routers.NestedSimpleRouter(
    router, r'users', lookup='user'
)

urlpatterns = [
    # Examples:
    # url(r'^$', 'Laplace.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^api/v1/', include(router.urls)),
    url(r'^api/v1', include(accounts_router.urls)),
    url(r'^admin/', include(admin.site.urls)),
]
