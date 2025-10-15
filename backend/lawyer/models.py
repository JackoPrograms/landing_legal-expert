from django.db import models
from django.utils.text import slugify


class Service(models.Model):
    """Юридическая услуга компании"""
    name = models.CharField("Название услуги", max_length=200)
    slug = models.SlugField("URL slug", max_length=200, unique=True, blank=True)
    icon = models.CharField("Иконка/Эмодзи", max_length=50, help_text="Эмодзи или иконка для карточки")
    short_description = models.TextField("Краткое описание", max_length=300, help_text="Для карточки на главной")
    description = models.TextField("Полное описание", blank=True)
    order = models.IntegerField("Порядок отображения", default=0)
    is_active = models.BooleanField("Активна", default=True)
    created = models.DateTimeField("Дата создания", auto_now_add=True)
    updated = models.DateTimeField("Дата обновления", auto_now=True)

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"
        ordering = ['order', 'name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class LawyerProfile(models.Model):
    """Профиль юриста компании"""
    full_name = models.CharField("ФИО", max_length=200)
    position = models.CharField("Должность", max_length=200)
    bio = models.TextField("Биография", help_text="Отображается при наведении на карточку")
    experience_text = models.CharField(
        "Текст об опыте",
        max_length=200,
        help_text="Например: '12 лет юридической практики'",
        blank=True
    )
    photo = models.ImageField("Фотография", upload_to='lawyers/', blank=True, null=True)
    phone = models.CharField("Телефон", max_length=20, blank=True)
    email = models.EmailField("Email", blank=True)
    specialization = models.ManyToManyField(
        Service,
        verbose_name="Специализация",
        related_name="lawyers",
        blank=True
    )
    order = models.IntegerField("Порядок отображения", default=0)
    is_active = models.BooleanField("Активен", default=True)
    created = models.DateTimeField("Дата создания", auto_now_add=True)
    updated = models.DateTimeField("Дата обновления", auto_now=True)

    class Meta:
        verbose_name = "Юрист"
        verbose_name_plural = "Юристы"
        ordering = ['order', 'full_name']

    def __str__(self):
        return f"{self.full_name} - {self.position}"


class Review(models.Model):
    """Отзыв клиента"""
    client_name = models.CharField("Имя клиента", max_length=200)
    client_company = models.CharField("Компания клиента", max_length=200, blank=True)
    text = models.TextField("Текст отзыва")
    photo = models.ImageField("Фото клиента", upload_to='reviews/', blank=True, null=True)
    date = models.CharField(
        "Дата отзыва (текст)",
        max_length=100,
        help_text="Например: 'Январь 2024'",
        blank=True
    )
    created = models.DateTimeField("Дата создания", auto_now_add=True)
    is_active = models.BooleanField("Активен", default=True)
    order = models.IntegerField("Порядок отображения", default=0)

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ['order', '-created']

    def __str__(self):
        return f"Отзыв от {self.client_name}"


class Article(models.Model):
    """Статья/Новость блога"""
    title = models.CharField("Заголовок", max_length=300)
    slug = models.SlugField("URL slug", max_length=300, unique=True, blank=True)
    excerpt = models.TextField("Краткое описание", max_length=500, help_text="Для карточки на главной")
    content = models.TextField("Полный текст статьи")
    image = models.ImageField("Изображение", upload_to='articles/')
    published_date = models.DateField("Дата публикации")
    created = models.DateTimeField("Дата создания", auto_now_add=True)
    updated = models.DateTimeField("Дата обновления", auto_now=True)
    is_published = models.BooleanField("Опубликована", default=True)
    views = models.IntegerField("Просмотры", default=0)

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ['-published_date']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class HeroSlide(models.Model):
    """Слайд главного баннера"""
    title = models.CharField("Заголовок", max_length=300)
    subtitle = models.CharField("Подзаголовок", max_length=500, blank=True)
    button_text = models.CharField("Текст кнопки", max_length=100, default="Записаться на консультацию")
    button_link = models.CharField(
        "Ссылка кнопки",
        max_length=200,
        default="#contact",
        help_text="Например: #contact или /services/"
    )
    background_image = models.ImageField("Фоновое изображение", upload_to='hero/')
    order = models.IntegerField("Порядок отображения", default=0)
    is_active = models.BooleanField("Активен", default=True)

    class Meta:
        verbose_name = "Слайд баннера"
        verbose_name_plural = "Слайды баннера"
        ordering = ['order']

    def __str__(self):
        return self.title


class ContactRequest(models.Model):
    """Заявка на консультацию"""
    STATUS_CHOICES = [
        ('new', 'Новая'),
        ('in_progress', 'В работе'),
        ('completed', 'Завершена'),
    ]

    name = models.CharField("Имя", max_length=200)
    phone = models.CharField("Телефон", max_length=20)
    email = models.EmailField("Email", blank=True)
    service = models.ForeignKey(
        Service,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Выбранная услуга",
        related_name="requests"
    )
    message = models.TextField("Сообщение", blank=True)
    status = models.CharField("Статус", max_length=20, choices=STATUS_CHOICES, default='new')
    created = models.DateTimeField("Дата создания", auto_now_add=True)

    class Meta:
        verbose_name = "Заявка на консультацию"
        verbose_name_plural = "Заявки на консультацию"
        ordering = ['-created']

    def __str__(self):
        return f"Заявка от {self.name} - {self.created.strftime('%d.%m.%Y %H:%M')}"


class CompanyInfo(models.Model):
    """Информация о компании (singleton)"""
    company_name = models.CharField("Название компании", max_length=200, default="ПРАВОЗАЩИТНИК")
    slogan = models.CharField("Слоган", max_length=300, blank=True)
    description = models.TextField("Описание компании", help_text="Для секции 'О компании'")
    phone = models.CharField("Телефон", max_length=20)
    email = models.EmailField("Email")
    address = models.CharField("Адрес", max_length=500, blank=True)
    
    # Социальные сети
    vk_link = models.URLField("Ссылка на VK", blank=True)
    telegram_link = models.URLField("Ссылка на Telegram", blank=True)
    whatsapp_link = models.CharField("WhatsApp (номер)", max_length=20, blank=True)
    
    # SEO
    meta_title = models.CharField("SEO заголовок", max_length=200, blank=True)
    meta_description = models.TextField("SEO описание", max_length=300, blank=True)
    
    created = models.DateTimeField("Дата создания", auto_now_add=True)
    updated = models.DateTimeField("Дата обновления", auto_now=True)

    class Meta:
        verbose_name = "Информация о компании"
        verbose_name_plural = "Информация о компании"

    def __str__(self):
        return self.company_name

    def save(self, *args, **kwargs):
        # Singleton pattern - только одна запись
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def get_instance(cls):
        """Получить единственную запись"""
        obj, created = cls.objects.get_or_create(pk=1)
        return obj
