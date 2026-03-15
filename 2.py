class UnderageError(Exception):
    pass

class InvalidAgeError(Exception):
    pass

def check_age(age):
    try:
        age = int(age)
        
        if age < 0 or age > 150:
            raise InvalidAgeError(f"Некорректный возраст: {age}. Возраст должен быть от 0 до 150 лет")
        
        if age < 18:
            raise UnderageError(f"Доступ запрещен! Вам {age} лет. Фильм доступен только с 18 лет")
        
        print(f"Доступ разрешен! Ваш возраст: {age} лет. Приятного просмотра!")
        return True
        
    except ValueError:
        raise InvalidAgeError("Ошибка! Возраст должен быть числом")

def age_censor():
    print("=== ВОЗРАСТНОЙ ЦЕНЗОР ===")
    print("Проверка возраста для просмотра фильма 18+")
    
    while True:
        try:
            age_input = input("\nВведите ваш возраст (или 'exit' для выхода): ")
            
            if age_input.lower() == 'exit':
                print("Программа завершена. До свидания!")
                break
            
            check_age(age_input)
            
        except (UnderageError, InvalidAgeError) as e:
            print(f"✗ {e}")
        except KeyboardInterrupt:
            print("\nПрограмма прервана пользователем")
            break
