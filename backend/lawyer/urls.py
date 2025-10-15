from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ServiceViewSet, LawyerProfileViewSet, ReviewViewSet,
    ArticleViewSet, HeroSlideViewSet, ContactRequestViewSet,
    CompanyInfoView
)

# Создаем роутер для ViewSets
router = DefaultRouter()
router.register(r'services', ServiceViewSet, basename='service')
router.register(r'lawyers', LawyerProfileViewSet, basename='lawyer')
router.register(r'reviews', ReviewViewSet, basename='review')
router.register(r'articles', ArticleViewSet, basename='article')
router.register(r'hero-slides', HeroSlideViewSet, basename='heroslide')
router.register(r'contact-requests', ContactRequestViewSet, basename='contactrequest')

urlpatterns = [
    path('', include(router.urls)),
    path('company-info/', CompanyInfoView.as_view(), name='company-info'),
]


