#!/bin/bash

# Підготовка до деплою
echo "🚀 Починаю підготовку до деплою..."

# Видаляємо кеш-файли
echo "🧹 Видаляю кеш та невикористовувані файли..."
find . -name '.DS_Store' -delete
find . -name '__MACOSX' -exec rm -rf {} +
find . -name '*.pyc' -delete
find . -name '__pycache__' -exec rm -rf {} +

# Перевіряємо наявність важливих файлів
echo "🔍 Перевіряю наявність критичних файлів..."
if [ ! -f "passenger_wsgi.py" ]; then
    echo "❌ passenger_wsgi.py відсутній!"
    exit 1
fi

if [ ! -f ".htaccess" ]; then
    echo "❌ .htaccess відсутній!"
    exit 1
fi

if [ ! -f "env_template.txt" ]; then
    echo "❌ env_template.txt відсутній!"
    exit 1
fi

# Збираємо статичні файли
echo "📦 Збираю статичні файли..."
if [ -d "venv" ]; then
    source venv/bin/activate
    python manage.py collectstatic --noinput
    deactivate
else
    echo "⚠️ Віртуальне середовище 'venv' не знайдено! Пропускаю збір статичних файлів."
fi

# Створюємо архів
echo "📁 Створюю архів для деплою..."
zip -r airinua_deploy.zip . -x "*.git*" "*.DS_Store" "*__pycache__*" "*.pyc" "venv/*" "*.zip" "logs/*" "staticfiles/*"

echo "✅ Підготовка до деплою завершена!"
echo "📋 Наступні кроки:"
echo "1. Завантажте 'airinua_deploy.zip' на ваш хостинг"
echo "2. Розпакуйте архів в кореневу папку сайту"
echo "3. Оновіть шлях до Python інтерпретатора в passenger_wsgi.py"
echo "4. Створіть файл .env на основі env_template.txt"
echo "5. Створіть віртуальне середовище та встановіть залежності"
echo "6. Запустіть міграції та збір статичних файлів"
echo "7. Налаштуйте Python App у cPanel"
echo "8. Перевірте роботу сайту" 