from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HeroViewSet, TankViewSet, DamageDealerViewSet, SupportViewSet,CounterViewSet, character_list, tank_detail, dd_detail, support_detail

router = DefaultRouter()
router.register(r'tanks', TankViewSet)
router.register(r'damagedealers', DamageDealerViewSet)
router.register(r'supports', SupportViewSet)
router.register(r'heroes', HeroViewSet)
router.register(r'counters', CounterViewSet)

urlpatterns = [
    path('characters/', character_list, name='character-list'),
    path('', include(router.urls)),
    path('tanks/<int:pk>/', TankViewSet.as_view({'get': 'retrieve'}), name='tank-detail'),
    path('damagedealers/<int:pk>/', DamageDealerViewSet.as_view({'get': 'retrieve'}), name='damagedealer-detail'),
    path('supports/<int:pk>/', SupportViewSet.as_view({'get': 'retrieve'}), name='support-detail'),
    path('tank_detail/<int:pk>/', tank_detail, name='tank-detail'),
    path('damagedealer_detail/<int:pk>/',dd_detail , name='damagedealer-detail'),
    path('support_detail/<int:pk>/',support_detail , name='support-detail'),
]
