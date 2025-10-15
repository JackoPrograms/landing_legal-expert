from rest_framework import serializers
from .models import Service, LawyerProfile, Review, Article, HeroSlide, ContactRequest, CompanyInfo


class ServiceSerializer(serializers.ModelSerializer):
    """Сериализатор для услуг"""
    class Meta:
        model = Service
        fields = ['id', 'name', 'slug', 'icon', 'short_description', 'description', 'order']


class LawyerProfileSerializer(serializers.ModelSerializer):
    """Сериализатор для профилей юристов"""
    specialization = ServiceSerializer(many=True, read_only=True)
    photo_url = serializers.SerializerMethodField()
    
    class Meta:
        model = LawyerProfile
        fields = [
            'id', 'full_name', 'position', 'bio', 'experience_text',
            'photo', 'photo_url', 'phone', 'email', 'specialization', 'order'
        ]
    
    def get_photo_url(self, obj):
        if obj.photo:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.photo.url)
        return None


class ReviewSerializer(serializers.ModelSerializer):
    """Сериализатор для отзывов"""
    photo_url = serializers.SerializerMethodField()
    
    class Meta:
        model = Review
        fields = [
            'id', 'client_name', 'client_company', 'text',
            'photo', 'photo_url', 'date', 'order'
        ]
    
    def get_photo_url(self, obj):
        if obj.photo:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.photo.url)
        return None


class ArticleSerializer(serializers.ModelSerializer):
    """Сериализатор для статей"""
    image_url = serializers.SerializerMethodField()
    
    class Meta:
        model = Article
        fields = [
            'id', 'title', 'slug', 'excerpt', 'content',
            'image', 'image_url', 'published_date', 'views'
        ]
    
    def get_image_url(self, obj):
        if obj.image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.image.url)
        return None


class ArticleListSerializer(serializers.ModelSerializer):
    """Сериализатор для списка статей (без полного контента)"""
    image_url = serializers.SerializerMethodField()
    
    class Meta:
        model = Article
        fields = ['id', 'title', 'slug', 'excerpt', 'image', 'image_url', 'published_date', 'views']
    
    def get_image_url(self, obj):
        if obj.image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.image.url)
        return None


class HeroSlideSerializer(serializers.ModelSerializer):
    """Сериализатор для слайдов баннера"""
    background_image_url = serializers.SerializerMethodField()
    
    class Meta:
        model = HeroSlide
        fields = [
            'id', 'title', 'subtitle', 'button_text', 'button_link',
            'background_image', 'background_image_url', 'order'
        ]
    
    def get_background_image_url(self, obj):
        if obj.background_image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.background_image.url)
        return None


class ContactRequestSerializer(serializers.ModelSerializer):
    """Сериализатор для заявок на консультацию"""
    class Meta:
        model = ContactRequest
        fields = ['id', 'name', 'phone', 'email', 'service', 'message', 'created']
        read_only_fields = ['created']


class CompanyInfoSerializer(serializers.ModelSerializer):
    """Сериализатор для информации о компании"""
    class Meta:
        model = CompanyInfo
        fields = [
            'id', 'company_name', 'slogan', 'description',
            'phone', 'email', 'address',
            'vk_link', 'telegram_link', 'whatsapp_link',
            'meta_title', 'meta_description'
        ]


