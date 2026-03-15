class PasswordTooShortError(Exception):
    pass

class NoDigitError(Exception):
    pass

class NoUppercaseError(Exception):
    pass

class NoLowercaseError(Exception):
    pass

def validate_password(password):
    if len(password) < 8:
        raise PasswordTooShortError(f"Пароль слишком короткий. Минимальная длина: 8 символов, получено: {len(password)}")
    
    if not any(char.isdigit() for char in password):
        raise NoDigitError("Пароль должен содержать хотя бы одну цифру")
    
    if not any(char.isupper() for char in password):
        raise NoUppercaseError("Пароль должен содержать хотя бы одну заглавную букву")
    
    if not any(char.islower() for char in password):
        raise NoLowercaseError("Пароль должен содержать хотя бы одну строчную букву")
    
    return True
