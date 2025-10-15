# 🎨 Frontend Setup Guide

## Установка и запуск

### 1. Установка зависимостей

```bash
npm install
```

### 2. Запуск dev сервера

```bash
npm run dev
```

Приложение будет доступно по адресу: http://localhost:5173

### 3. Production build

```bash
npm run build
```

Готовые файлы появятся в папке `dist/`

### 4. Предпросмотр production build

```bash
npm run preview
```

## Конфигурация

### vite.config.js

Настроен proxy для подключения к Django backend:

```javascript
server: {
  port: 5173,
  proxy: {
    '/api': {
      target: 'http://127.0.0.1:8000',
      changeOrigin: true,
    },
    '/media': {
      target: 'http://127.0.0.1:8000',
      changeOrigin: true,
    }
  }
}
```

## Структура проекта

```
src/
├── components/           # Компоненты
│   ├── AppHeader.vue    # Шапка сайта
│   ├── AppFooter.vue    # Подвал
│   ├── HeroSection.vue  # Главный баннер (слайдер)
│   ├── ServicesSection.vue    # Секция услуг
│   ├── AboutSection.vue       # О компании
│   ├── LawyersSection.vue     # Команда юристов
│   ├── ReviewsSection.vue     # Отзывы (карусель)
│   ├── ArticlesSection.vue    # Блог/новости
│   └── ContactModal.vue       # Форма обратной связи
│
├── views/                # Страницы
│   └── HomePage.vue      # Главная страница
│
├── stores/               # Pinia хранилища
│   └── lawyer.js         # State management
│
├── services/             # API сервисы
│   └── api.js            # HTTP запросы
│
├── router/               # Vue Router
│   └── index.js          # Маршрутизация
│
├── assets/               # Стили
│   └── main.css          # Глобальные стили
│
├── App.vue               # Корневой компонент
└── main.js               # Точка входа
```

## Основные компоненты

### AppHeader
- Верхняя панель с контактами
- Логотип компании
- Навигация (Desktop)
- Бургер-меню (Mobile)
- Кнопка "Записаться онлайн"

### AppFooter
- 4 колонки с информацией
- Список услуг
- Контактные данные
- Карточка юриста
- Копирайт

### HeroSection
- Swiper слайдер
- Автопрокрутка
- Навигация стрелками и точками
- Адаптивная высота

### ServicesSection
- Сетка карточек 3x2 (Desktop)
- Hover эффекты
- Адаптивность

### AboutSection
- 2-колоночный layout
- Текст и изображение
- Кнопки действий

### LawyersSection
- Сетка карточек 3 колонки
- Overlay с биографией при наведении
- Информация о специализации

### ReviewsSection
- Swiper карусель
- Адаптивное количество слайдов
- Автопрокрутка

### ArticlesSection
- Сетка карточек 3 колонки
- Hover эффект на изображениях
- Дата публикации и просмотры

### ContactModal
- Teleport в body
- Форма с валидацией
- Отправка на API
- Уведомления об успехе/ошибке

## State Management (Pinia)

### Store: lawyer.js

**State:**
- services - список услуг
- lawyers - список юристов
- reviews - список отзывов
- articles - список статей
- heroSlides - слайды баннера
- companyInfo - информация о компании
- loading - индикатор загрузки
- error - ошибки

**Actions:**
- fetchServices()
- fetchLawyers()
- fetchReviews()
- fetchArticles()
- fetchHeroSlides()
- fetchCompanyInfo()
- sendContactRequest(data)
- loadAllData() - загрузка всех данных сразу

## API Service

### api.js

Все API методы централизованы:

```javascript
// Услуги
getServices()
getService(slug)

// Юристы
getLawyers()

// Отзывы
getReviews()

// Статьи
getArticles(page)
getArticle(slug)

// Слайды
getHeroSlides()

// Компания
getCompanyInfo()

// Заявки
sendContactRequest(data)
```

## Стили

### main.css

Глобальные стили с CSS переменными:

```css
:root {
  --primary-color: #4A90E2;
  --dark-color: #2C2C2C;
  --text-dark: #333333;
  --text-light: #666666;
  --bg-light: #F5F5F5;
  --white: #FFFFFF;
  ...
}
```

### Шрифт
Google Fonts - Nunito Sans (300, 400, 600, 700, 800)

### Breakpoints
- Desktop: 1200px+
- Tablet: 768px-1199px
- Mobile: до 767px

## Разработка

### Запуск с Backend

1. **Terminal 1 - Backend:**
```bash
cd backend
.\venv\Scripts\activate  # Windows
python manage.py runserver
```

2. **Terminal 2 - Frontend:**
```bash
cd frontend
npm run dev
```

3. Откройте http://localhost:5173

### Hot Module Replacement (HMR)

Vite автоматически перезагружает изменения без обновления страницы.

## Troubleshooting

### Не загружаются данные

1. Проверьте, что backend запущен на http://127.0.0.1:8000
2. Проверьте браузерную консоль на ошибки
3. Убедитесь, что CORS настроен правильно в Django

### Ошибка 404 на API запросах

Проверьте proxy настройки в vite.config.js

### Swiper не работает

```bash
npm install swiper
```

### Ошибка "Cannot find module 'vue'"

```bash
npm install vue@3
```

### Стили не применяются

1. Проверьте импорт в main.js: `import './assets/main.css'`
2. Проверьте scoped атрибуты в компонентах

## Production Deployment

### Сборка

```bash
npm run build
```

### Файлы для деплоя

Загрузите содержимое папки `dist/` на хостинг.

### Рекомендуемые хостинги

- **Netlify** - бесплатно, автодеплой
- **Vercel** - бесплатно, отличная производительность
- **GitHub Pages** - бесплатно
- **Cloudflare Pages** - бесплатно, глобальный CDN

### Переменные окружения для production

Создайте `.env.production`:

```
VITE_API_URL=https://your-backend-domain.com
```

И обновите api.js:

```javascript
const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL || '/api/lawyer',
  ...
})
```


