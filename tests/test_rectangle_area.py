import pytest
from app.geometry.rectangle_area import rectangle_area


def test_rectangle_area_corrert_lenght():
    """
    Проверка целых положительных значений длин сторон прямоугольника
    """
    # Arrange
    width = "3"
    height = "5"
    expected_result = 15
    
    # Act
    actual_result = rectangle_area(width, height)
    
    # Assert
    assert actual_result == pytest.approx(expected_result)

def test_rectangle_area_string_date():
    """""
    Тестирование вычесление площади со строкой в качестве длины прямоугольника
    """

    width = "hello"
    height = "5.2"
    with pytest.raises(ValueError) as exc_info:
        rectangle_area(width, height)
    assert str(exc_info.value) == "Введено не числовое значение стороны"


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