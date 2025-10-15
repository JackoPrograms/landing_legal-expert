from rest_framework import viewsets, generics, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Service, LawyerProfile, Review, Article, HeroSlide, ContactRequest, CompanyInfo
from .serializers import (
    ServiceSerializer, LawyerProfileSerializer, ReviewSerializer,
    ArticleSerializer, ArticleListSerializer, HeroSlideSerializer,
    ContactRequestSerializer, CompanyInfoSerializer
)


class ServiceViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet для услуг (только чтение)"""
    queryset = Service.objects.filter(is_active=True)
    serializer_class = ServiceSerializer
    lookup_field = 'slug'


class LawyerProfileViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet для профилей юристов (только чтение)"""
    queryset = LawyerProfile.objects.filter(is_active=True).prefetch_related('specialization')
    serializer_class = LawyerProfileSerializer


class ReviewViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet для отзывов (только чтение)"""
    queryset = Review.objects.filter(is_active=True)
    serializer_class = ReviewSerializer


class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet для статей (только чтение)"""
    queryset = Article.objects.filter(is_published=True)
    lookup_field = 'slug'
    
    def get_serializer_class(self):
        if self.action == 'list':
            return ArticleListSerializer
        return ArticleSerializer
    
    def retrieve(self, request, *args, **kwargs):
        """Увеличиваем счетчик просмотров при просмотре статьи"""
        instance = self.get_object()
        instance.views += 1
        instance.save(update_fields=['views'])
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class HeroSlideViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet для слайдов баннера (только чтение)"""
    queryset = HeroSlide.objects.filter(is_active=True)
    serializer_class = HeroSlideSerializer


class ContactRequestViewSet(viewsets.ModelViewSet):
    """ViewSet для заявок на консультацию"""
    queryset = ContactRequest.objects.all()
    serializer_class = ContactRequestSerializer
    
    # Разрешаем только создание (POST) для публичного доступа
    http_method_names = ['post']


class CompanyInfoView(generics.RetrieveAPIView):
    """View для получения информации о компании"""
    serializer_class = CompanyInfoSerializer
    
    def get_object(self):
        return CompanyInfo.get_instance()
