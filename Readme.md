# 🧠 NeuroShop — Django-платформа для генерации и публикации AI-контента

**NeuroShop** — это современный веб-сайт, созданный на Django, с функциями блога, видео-контента, загрузки изображений и комментариев. Подходит для магазинов, медиа-хабов и проектов с акцентом на ИИ-генерируемый контент.

---

## 🚀 Функциональность

### 📚 Блог
- Публикация постов с изображениями
- Поддержка тегов через `django-taggit`
- Комментарии от авторизованных пользователей
- Постраничная навигация (по 9 постов на страницу)
- Отображение миниатюр и краткого описания

### 🗂 Теги
- Список тегов под каждым постом
- Фильтрация постов по выбранному тегу

### 🧾 Обратная связь
- Форма оценки, отзывов и предложений
- Сохранение данных от пользователей
- Спасибо-страница

### 🎬 Видео
- Воспроизведение 2 видеофрагментов `.mp4`
- Кастомные заставки (poster) к каждому ролику
- Загружаются из папки `/media/videos/` и `/media/posters/`

### 🔐 Авторизация
- Регистрация / Вход / Выход
- Отображение меню в зависимости от статуса пользователя
- Панель администратора для управления контентом

---

## 📁 Структура проекта

NeuroShop/
├── app/
│   ├── templates/app/
│   ├── static/app/
│   ├── models.py
│   ├── views.py
│   └── forms.py
├── media/
│   ├── blog_images/
│   ├── videos/
│   └── posters/
├── static/
├── templates/
├── manage.py
└── requirements.txt

---

## 🛠 Установка

```bash
git clone https://github.com/yourusername/neuroshop.git
cd neuroshop
python -m venv venv
venv\Scripts\activate         # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
🧩 Зависимости
Python 3.9+

Django 4.x

Pillow

django-taggit

Bootstrap 5.3 (CDN)

SQLite (по умолчанию)

🔐 Админ-доступ
bash
Копировать
Редактировать
python manage.py createsuperuser

⚖️ Лицензия
Проект распространяется под лицензией MIT.
Автор: @yourusername
