## Установка
### 1. Установить зависимости (только macOS / Linux)
Если вы используете macOS или Linux, убедитесь, что в вашей системе установлены основные бинарные файлы GDAL:
* **macOS (Homebrew)**: `brew install gdal`
* **Linux (Ubuntu/Debian)**: `sudo apt-get install libgdal-dev`
* **Windows**: Пропустите этот шаг.

### 2. Настроить среду Python
Используйте следующие команды для установки нужных библиотек:

```bash
# Install standard dependencies and the installation utility
pip install -r requirements.txt

# Run the installer tool to link GDAL to your Python environment
gdal-installer
```
