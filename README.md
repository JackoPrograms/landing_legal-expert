# 🏛️ ПРАВОЗАЩИТНИК - Юридическая компания

Полнофункциональный веб-сайт юридической компании с современным дизайном и админ-панелью.

## 📋 Описание проекта

Профессиональный корпоративный сайт для юридической компании с:
- Представлением услуг компании
- Профилями команды юристов
- Отзывами клиентов
- Блогом с полезными материалами
- Формой обратной связи
- Полной адаптивностью (Desktop, Tablet, Mobile)
- Админ-панелью для управления контентом

## 🛠 Технологический стек

### Backend
- **Django 5.2** - Python веб-фреймворк
- **Django REST Framework** - для создания REST API
- **SQLite** (разработка) / **PostgreSQL** (продакшн)
- **django-cors-headers** - для работы с CORS
- **Pillow** - для обработки изображений

### Frontend
- **Vue.js 3** - прогрессивный JavaScript фреймворк
- **Vite** - быстрый сборщик проекта
- **Pinia** - управление состоянием
- **Vue Router** - маршрутизация
- **Axios** - HTTP клиент
- **Swiper.js** - слайдеры и карусели

## 📁 Структура проекта

```
lawyer_project_documentation/
├── backend/                    # Django Backend
│   ├── lawyer/                 # Основное приложение
│   │   ├── models.py          # Модели данных
│   │   ├── serializers.py     # DRF сериализаторы
│   │   ├── views.py           # API views
│   │   ├── urls.py            # URL маршруты
│   │   └── admin.py           # Админ-панель
│   ├── lawyer_project/        # Настройки проекта
│   ├── manage.py              # Django CLI
│   ├── requirements.txt       # Python зависимости
│   └── db.sqlite3            # База данных (SQLite)
│
├── frontend/                  # Vue.js Frontend
│   ├── src/
│   │   ├── components/       # Vue компоненты
│   │   │   ├── AppHeader.vue
│   │   │   ├── AppFooter.vue
│   │   │   ├── HeroSection.vue
│   │   │   ├── ServicesSection.vue
│   │   │   ├── AboutSection.vue
│   │   │   ├── LawyersSection.vue
│   │   │   ├── ReviewsSection.vue
│   │   │   ├── ArticlesSection.vue
│   │   │   └── ContactModal.vue
│   │   ├── views/            # Страницы
│   │   │   └── HomePage.vue
│   │   ├── stores/           # Pinia хранилища
│   │   │   └── lawyer.js
│   │   ├── services/         # API сервисы
│   │   │   └── api.js
│   │   ├── router/           # Vue Router
│   │   │   └── index.js
│   │   ├── assets/           # Стили и ресурсы
│   │   │   └── main.css
│   │   ├── App.vue           # Корневой компонент
│   │   └── main.js           # Точка входа
│   ├── package.json
│   └── vite.config.js
│
└── PROJECT_GUIDE.md          # Полная документация проекта
```

## 🚀 Быстрый старт

### Требования

- Python 3.9+
- Node.js 18+
- npm или yarn

### Установка Backend

1. Перейдите в директорию backend:
```bash
cd backend
```

2. Создайте и активируйте виртуальное окружение:
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/MacOS
python3 -m venv venv
source venv/bin/activate
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

4. Создайте суперпользователя:
```bash
python manage.py createsuperuser
```

5. Запустите сервер разработки:
```bash
python manage.py runserver
```

Backend будет доступен по адресу: http://127.0.0.1:8000
Админ-панель: http://127.0.0.1:8000/admin
API: http://127.0.0.1:8000/api/lawyer/

### Установка Frontend

1. Перейдите в директорию frontend:
```bash
cd frontend
```

2. Установите зависимости:
```bash
npm install
```

3. Запустите dev сервер:
```bash
npm run dev
```

Frontend будет доступен по адресу: http://localhost:5173

## 📊 API Endpoints

### Основные endpoints:

```
GET  /api/lawyer/services/              - Список услуг
GET  /api/lawyer/services/{slug}/       - Конкретная услуга

GET  /api/lawyer/lawyers/               - Список юристов

GET  /api/lawyer/reviews/               - Список отзывов

GET  /api/lawyer/articles/              - Список статей (с пагинацией)
GET  /api/lawyer/articles/{slug}/       - Конкретная статья

GET  /api/lawyer/hero-slides/           - Слайды главного баннера

GET  /api/lawyer/company-info/          - Информация о компании

POST /api/lawyer/contact-requests/      - Создание заявки на консультацию
```

## 🎨 Функционал

### Для посетителей:
- ✅ Просмотр услуг компании
- ✅ Знакомство с командой юристов
- ✅ Чтение отзывов клиентов
- ✅ Изучение блога/новостей
- ✅ Отправка заявки на консультацию
- ✅ Адаптивный дизайн для всех устройств

### Для администраторов:
- ✅ Управление услугами
- ✅ Управление профилями юристов
- ✅ Модерация отзывов
- ✅ Публикация статей
- ✅ Настройка слайдов баннера
- ✅ Обработка заявок клиентов
- ✅ Редактирование информации о компании

## 📝 Управление контентом

Для добавления контента:

1. Войдите в админ-панель: http://127.0.0.1:8000/admin
2. Используйте созданные учетные данные суперпользователя
3. Добавьте:
   - Информацию о компании (CompanyInfo)
   - Услуги (Services)
   - Профили юристов (LawyerProfile)
   - Отзывы (Reviews)
   - Статьи (Articles)
   - Слайды баннера (HeroSlides)

## 🎯 Production Build

### Backend

1. Настройте production settings:
   - DEBUG = False
   - ALLOWED_HOSTS = ['your-domain.com']
   - Настройте PostgreSQL
   - Настройте SECRET_KEY из переменных окружения

2. Соберите статические файлы:
```bash
python manage.py collectstatic
```

3. Используйте Gunicorn + Nginx для деплоя

### Frontend

1. Создайте production build:
```bash
npm run build
```

2. Деплойте папку `dist/` на хостинг (Netlify, Vercel, или свой сервер)

## 📚 Дополнительная документация

Подробная документация доступна в файле [PROJECT_GUIDE.md](PROJECT_GUIDE.md), включая:
- Детальное описание архитектуры
- Описание всех моделей данных
- Руководство по дизайн-системе
- Пошаговый план разработки
- Инструкции по развёртыванию

## 🔒 Безопасность

- CORS настроен для разработки
- Валидация данных на backend
- Защита от XSS и CSRF
- Безопасное хранение паролей

## 📞 Поддержка

При возникновении вопросов:
1. Проверьте [PROJECT_GUIDE.md](PROJECT_GUIDE.md)
2. Изучите логи сервера/браузера
3. Проверьте документацию Django и Vue.js

## 📄 Лицензия

Этот проект создан для образовательных целей.

---

**Удачи в разработке! 🚀**


