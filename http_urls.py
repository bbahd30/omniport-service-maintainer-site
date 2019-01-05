from rest_framework import routers
from django.urls import path, include
from maintainer_site.views.blog import BlogsView
from maintainer_site.views.project import ProjectViewSet
from maintainer_site.views.social_information import SocialInformationView
from maintainer_site.views.location_information import LocationInformationView
from maintainer_site.views.contact_information import ContactInformationView
from maintainer_site.views.maintainer_group import MaintainerGroupView
from maintainer_site.views.maintainer_info import ActiveMaintainerInfoViewSet,MaintainerInfoViewSet,InactiveMaintainerInfoViewSet
from maintainer_site.views.social_link import SocialLinkViewSet
from maintainer_site.views.logged_maintainer import LoggedMaintainerViewSet

router = routers.SimpleRouter()
router.register('projects', ProjectViewSet, base_name='project')
router.register('active_maintainer_info', ActiveMaintainerInfoViewSet, base_name='active_maintainer_info')
router.register('inactive_maintainer_info', InactiveMaintainerInfoViewSet, base_name='inactive_maintainer_info')
router.register(r'social_link', SocialLinkViewSet, base_name="SocialLink")
router.register('logged_maintainer', LoggedMaintainerViewSet, base_name="LoggedMaintainer") 
urlpatterns = [
        path('blogs/', BlogsView.as_view()),
        path('social/', SocialInformationView.as_view()),
        path('location/', LocationInformationView.as_view()),
        path('contact/', ContactInformationView.as_view()),
        path('maintainer_group/', MaintainerGroupView.as_view()),
        path('', include(router.urls)),
]
