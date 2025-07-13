import requests

def get_weather(latitude, longitude):
    """
    Получает текущую погоду для заданных координат.
    Использует Open-Meteo API.
    """
    base_url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,weather_code,wind_speed_10m",
        "hourly": "temperature_2m", # Можно убрать, если не нужно
        "forecast_days": 1,
        "timezone": "auto" # Автоматически определяет часовой пояс
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status() # Вызывает исключение для ошибок HTTP (4xx или 5xx)
        data = response.json()

        # Извлечение текущей погоды
        current_data = data.get("current", {})
        temperature = current_data.get("temperature_2m")
        weather_code = current_data.get("weather_code")
        wind_speed = current_data.get("wind_speed_10m")
        units = data.get("current_units", {})
        temp_unit = units.get("temperature_2m", "°C")
        wind_unit = units.get("wind_speed_10m", "m/s")

        # Перевод кода погоды в понятное описание (упрощенный вариант)
        weather_description = "Неизвестно"
        if weather_code is not None:
            if weather_code == 0:
                weather_description = "Ясно"
            elif 1 <= weather_code <= 3:
                weather_description = "Переменная облачность"
            elif 45 <= weather_code <= 48:
                weather_description = "Туман"
            elif 51 <= weather_code <= 60:
                weather_description = "Морось"
            elif 61 <= weather_code <= 65:
                weather_description = "Дождь"
            elif 66 <= weather_code <= 67:
                weather_description = "Ледяной дождь"
            elif 71 <= weather_code <= 75:
                weather_description = "Снег"
            elif 80 <= weather_code <= 82:
                weather_description = "Ливни"
            elif 95 <= weather_code <= 99:
                weather_description = "Гроза"

        print(f"Погода:")
        print(f"  Температура: {temperature}{temp_unit}")
        print(f"  Условия: {weather_description}")
        print(f"  Скорость ветра: {wind_speed}{wind_unit}")

    except requests.exceptions.RequestException as e:
        print(f"Ошибкdfdfа при запросе gghgпогоды: {e}")
    except KeyError as e:
        print(f"Ошибка при парсфwewesddвzxыввыууунге данных: Отсутствует ключ {e}")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")

# --- Использование скрипта ---

if __name__ == "__main__":
    # Координаты для Алматы, Казахстан (пример)
    almaty_lat = 43.2567
    almaty_lon = 76.9286

    print("Получение погод2ы для Алматы:")
    get_weather(almaty_lat, almaty_lon)

    print("\nВведите свои координаты:")
    try:
        user_lat = float(input("Введите широту (например, 55.75): "))
        user_lon = float(input("Введите долготу (например, 37.61): "))
        get_weather(user_lat, user_lon)
    except ValueError:
        print("Некорректный ввод. Пожалуйста, введите числа для координат.")