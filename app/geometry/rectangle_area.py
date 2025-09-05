def parse_number(value: str) -> float:
    """
    проверка корректности ввода стороны треугольника
    :param value: пользовательский ввод длин сторон прямоугольника
    :return number: длина стороны треугольника (тип float)
    """
    try:
        input_data = value.strip().replace(',', '.')
        number = float(input_data)
    except ValueError:
        raise ValueError("Введено не числовое значение стороны")
    
    if number <= 0:
        raise ValueError("Сторона должна быть положительным числом") 
    
    return number
    
def rectangle_area(width: str, height: str) -> float:
    """
    Нахождение площади треугольника
    :param width: ширина прямоугольника
    :param height высота прямоугольника
    :return: площадь прямоугольника
    """
    
    w = parse_number(width)
    h = parse_number(height)
    return w * h