class InvalidTemperatureError(Exception):
    pass

def celsius_to_fahrenheit(celsius):
    try:
        celsius = float(celsius)
        
        if celsius < -273.15:
            raise InvalidTemperatureError(
                f"Температура {celsius}°C ниже абсолютного нуля (-273.15°C). "
                f"Введите корректную температуру."
            )
        
        fahrenheit = (celsius * 9/5) + 32
        return fahrenheit
        
    except ValueError:
        raise InvalidTemperatureError(f"Ошибка! '{celsius}' не является числом. Введите числовое значение температуры.")

def temperature_converter():
    print("=== КОНВЕРТЕР ТЕМПЕРАТУРЫ ===")
    print("Конвертация из Цельсия в Фаренгейты")
    
    while True:
        try:
            print("\n" + "="*40)
            temp_input = input("Введите температуру в Цельсиях (или 'exit' для выхода): ")
            
            if temp_input.lower() == 'exit':
                print("Программа завершена. До свидания!")
                break
            
            result = celsius_to_fahrenheit(temp_input)
            
            print(f"\nРезультат конвертации:")
            print(f"   {temp_input}°C = {result:.2f}°F")
            
        except InvalidTemperatureError as e:
            print(f"✗ {e}")
        except KeyboardInterrupt:
            print("\nПрограмма прервана пользователем")
            break
