## Установка
### 1. Установить зависимости (только macOS / Linux)
Если вы используете macOS или Linux, убедитесь, что в вашей системе установлены основные бинарные файлы GDAL:
* **macOS (Homebrew)**: `brew install gdal`
* **Linux (Ubuntu/Debian)**: `sudo apt-get install libgdal-dev`
* **Windows**: Пропустите этот шаг.

### 2. Настроить среду Python
Используйте следующие команды для установки нужных библиотек:

```bash
# Основная часть библиотек:
pip install -r requirements.txt

# Установка подходящей конфигурации библиотеки GDAL:
gdal-installer
```
