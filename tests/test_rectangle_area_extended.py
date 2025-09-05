import pytest
from app.geometry.rectangle_area import rectangle_area


def test_rectangle_area_simple_case():
    """
    Простой тест с маленькими числами
    """
    width = "2"
    height = "3"
    expected_result = 6
    
    actual_result = rectangle_area(width, height)
    
    assert actual_result == pytest.approx(expected_result)


def test_rectangle_area_large_numbers():
    """
    Тест с большими числами
    """
    width = "100"
    height = "200"
    expected_result = 20000
    
    actual_result = rectangle_area(width, height)
    
    assert actual_result == pytest.approx(expected_result)


def test_rectangle_area_one_as_side():
    """
    Тест когда одна сторона равна 1
    """
    width = "1"
    height = "5"
    expected_result = 5
    
    actual_result = rectangle_area(width, height)
    
    assert actual_result == pytest.approx(expected_result)


def test_rectangle_area_both_decimal():
    """
    Тест с двумя десятичными числами
    """
    width = "1.5"
    height = "2.5"
    expected_result = 3.75
    
    actual_result = rectangle_area(width, height)
    
    assert actual_result == pytest.approx(expected_result)


def test_rectangle_area_very_long_rectangle():
    """
    Тест с очень длинным прямоугольником
    """
    width = "0.5"
    height = "10"
    expected_result = 5.0
    
    actual_result = rectangle_area(width, height)
    
    assert actual_result == pytest.approx(expected_result)


def test_rectangle_area_with_zeros_after_dot():
    """
    Тест с нулями после точки
    """
    width = "3.0"
    height = "4.0"
    expected_result = 12.0
    
    actual_result = rectangle_area(width, height)
    
    assert actual_result == pytest.approx(expected_result)


def test_rectangle_area_mixed_input():
    """
    Тест с смешанным вводом (целое и десятичное)
    """
    width = "5"
    height = "2.5"
    expected_result = 12.5
    
    actual_result = rectangle_area(width, height)
    
    assert actual_result == pytest.approx(expected_result)


def test_rectangle_area_small_square():
    """
    Тест с маленьким квадратом
    """
    width = "2"
    height = "2"
    expected_result = 4
    
    actual_result = rectangle_area(width, height)
    
    assert actual_result == pytest.approx(expected_result)


def test_rectangle_area_big_square():
    """
    Тест с большим квадратом
    """
    width = "10"
    height = "10"
    expected_result = 100
    
    actual_result = rectangle_area(width, height)
    
    assert actual_result == pytest.approx(expected_result)


def test_rectangle_area_fraction_like():
    """
    Тест с числами похожими на дроби
    """
    width = "0.25"
    height = "4"
    expected_result = 1.0
    
    actual_result = rectangle_area(width, height)
    
    assert actual_result == pytest.approx(expected_result)


def test_rectangle_area_trailing_spaces():
    """
    Тест с пробелами в конце
    """
    width = "3   "
    height = "   4"
    expected_result = 12
    
    actual_result = rectangle_area(width, height)
    
    assert actual_result == pytest.approx(expected_result)


def test_rectangle_area_comma_both_sides():
    """
    Тест с запятыми в обеих сторонах
    """
    width = "2,5"
    height = "3,2"
    expected_result = 8.0
    
    actual_result = rectangle_area(width, height)
    
    assert actual_result == pytest.approx(expected_result)


def test_rectangle_area_very_small_result():
    """
    Тест с очень маленьким результатом
    """
    width = "0.01"
    height = "0.1"
    expected_result = 0.001
    
    actual_result = rectangle_area(width, height)
    
    assert actual_result == pytest.approx(expected_result)


def test_rectangle_area_only_negative_error():
    """
    Тест ошибки только с отрицательным числом
    """
    width = "-5"
    height = "3"
    with pytest.raises(ValueError) as exc_info:
        rectangle_area(width, height)
    assert str(exc_info.value) == "Сторона должна быть положительным числом"


def test_rectangle_area_both_negative_error():
    """
    Тест ошибки с двумя отрицательными числами
    """
    width = "-2"
    height = "-3"
    with pytest.raises(ValueError) as exc_info:
        rectangle_area(width, height)
    assert str(exc_info.value) == "Сторона должна быть положительным числом"


def test_rectangle_area_letters_error():
    """
    Тест ошибки с буквами
    """
    width = "abc"
    height = "5"
    with pytest.raises(ValueError) as exc_info:
        rectangle_area(width, height)
    assert str(exc_info.value) == "Введено не числовое значение стороны"


def test_rectangle_area_special_chars_error():
    """
    Тест ошибки со специальными символами
    """
    width = "3@#"
    height = "4"
    with pytest.raises(ValueError) as exc_info:
        rectangle_area(width, height)
    assert str(exc_info.value) == "Введено не числовое значение стороны"


def test_rectangle_area_mixed_text_error():
    """
    Тест ошибки со смешанным текстом
    """
    width = "3a5"
    height = "4"
    with pytest.raises(ValueError) as exc_info:
        rectangle_area(width, height)
    assert str(exc_info.value) == "Введено не числовое значение стороны"


def test_rectangle_area_space_only_error():
    """
    Тест ошибки с пробелами
    """
    width = "   "
    height = "4"
    with pytest.raises(ValueError) as exc_info:
        rectangle_area(width, height)
    assert str(exc_info.value) == "Введено не числовое значение стороны"


def test_rectangle_area_zero_height_error():
    """
    Тест ошибки с нулевой высотой
    """
    width = "5"
    height = "0"
    with pytest.raises(ValueError) as exc_info:
        rectangle_area(width, height)
    assert str(exc_info.value) == "Сторона должна быть положительным числом"