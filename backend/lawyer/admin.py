from django.contrib import admin
from django.utils.html import format_html
from .models import Service, LawyerProfile, Review, Article, HeroSlide, ContactRequest, CompanyInfo


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon', 'order', 'is_active', 'created']
    list_filter = ['is_active', 'created']
    search_fields = ['name', 'short_description', 'description']
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['order', 'name']
    list_editable = ['order', 'is_active']


@admin.register(LawyerProfile)
class LawyerProfileAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'position', 'photo_preview', 'order', 'is_active', 'created']
    list_filter = ['is_active', 'created']
    search_fields = ['full_name', 'position', 'bio']
    filter_horizontal = ['specialization']
    ordering = ['order', 'full_name']
    list_editable = ['order', 'is_active']
    
    def photo_preview(self, obj):
        if obj.photo:
            return format_html('<img src="{}" style="width: 50px; height: 50px; object-fit: cover; border-radius: 50%;" />', obj.photo.url)
        return '-'
    photo_preview.short_description = 'Фото'


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'client_company', 'date', 'order', 'is_active', 'created']
    list_filter = ['is_active', 'created']
    search_fields = ['client_name', 'client_company', 'text']
    ordering = ['order', '-created']
    list_editable = ['order', 'is_active']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'published_date', 'views', 'is_published', 'created']
    list_filter = ['is_published', 'published_date', 'created']
    search_fields = ['title', 'excerpt', 'content']
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['-published_date']
    list_editable = ['is_published']
    readonly_fields = ['views', 'created', 'updated']


@admin.register(HeroSlide)
class HeroSlideAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'is_active']
    list_filter = ['is_active']
    search_fields = ['title', 'subtitle']
    ordering = ['order']
    list_editable = ['order', 'is_active']


@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'service', 'status', 'created']
    list_filter = ['status', 'service', 'created']
    search_fields = ['name', 'phone', 'email', 'message']
    ordering = ['-created']
    list_editable = ['status']
    readonly_fields = ['created']
    
    def has_add_permission(self, request):
        # Запрещаем создание заявок через админку (только через API)
        return False


@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'phone', 'email', 'updated']
    readonly_fields = ['created', 'updated']
    
    def has_add_permission(self, request):
        # Разрешаем только одну запись
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)
    
    def has_delete_permission(self, request, obj=None):
        # Запрещаем удаление
        return False


# Настройка админ-панели
admin.site.site_header = "ПРАВОЗАЩИТНИК - Администрирование"
admin.site.site_title = "ПРАВОЗАЩИТНИК"
admin.site.index_title = "Управление сайтом"
