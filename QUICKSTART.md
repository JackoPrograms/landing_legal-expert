# ⚡ Быстрый старт проекта

## 🚀 Запуск за 5 минут

### 1️⃣ Backend (Django)

```bash
# Перейдите в директорию backend
cd backend

# Активируйте виртуальное окружение (уже создано)
.\venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

# Создайте суперпользователя
python manage.py createsuperuser

# Запустите сервер
python manage.py runserver
```

✅ Backend работает на: **http://127.0.0.1:8000**

### 2️⃣ Frontend (Vue.js)

Откройте **новый терминал**:

```bash
# Перейдите в директорию frontend
cd frontend

# Запустите dev сервер
npm run dev
```

✅ Frontend работает на: **http://localhost:5173**

### 3️⃣ Добавьте контент

1. Откройте админ-панель: **http://127.0.0.1:8000/admin**
2. Войдите с созданными учетными данными
3. Добавьте минимальный контент:
   - ✅ **Информация о компании** (обязательно!)
   - ✅ **6 услуг** (с иконками-эмодзи)
   - ✅ **3 юриста** (с фотографиями)
   - ✅ **3 отзыва**
   - ✅ **3 статьи**
   - ✅ **1-2 слайда баннера** (с фоновыми изображениями)

### 4️⃣ Готово!

Откройте: **http://localhost:5173** и наслаждайтесь работающим сайтом! 🎉

---

## 📚 Подробные инструкции

- **Backend:** см. [backend/SETUP.md](backend/SETUP.md)
- **Frontend:** см. [frontend/SETUP.md](frontend/SETUP.md)
- **Полная документация:** см. [PROJECT_GUIDE.md](PROJECT_GUIDE.md)

---

## 🆘 Проблемы?

### Backend не запускается
```bash
cd backend
.\venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
```

### Frontend не запускается
```bash
cd frontend
npm install
npm run dev
```

### Данные не загружаются
1. Убедитесь, что backend работает на порту 8000
2. Добавьте контент через админ-панель
3. Проверьте консоль браузера (F12)

---

## 🎯 Порты по умолчанию

- **Backend (Django):** http://127.0.0.1:8000
- **Admin Panel:** http://127.0.0.1:8000/admin
- **API:** http://127.0.0.1:8000/api/lawyer/
- **Frontend (Vue):** http://localhost:5173

---

**Приятной разработки! 💻✨**


