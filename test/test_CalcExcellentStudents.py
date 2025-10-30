# -*- coding: utf-8 -*-
from src.Types import DataType
from src.CalcExcellentStudents import CalcExcellentStudents
import pytest

class TestCalcExcellentStudents:
    
    @pytest.fixture()
    def input_data(self) -> tuple[DataType, int]:
        data = {
            "Иванов Иван Иванович": [
                ("математика", 95),
                ("программирование", 92),
                ("литература", 90)
            ],
            "Петров Петр Петрович": [
                ("математика", 85),
                ("химия", 80)
            ],
            "Сидоров Сидор Сидорович": [
                ("физика", 95),
                ("математика", 96),
                ("химия", 94)
            ],
            "Кузнецов Алексей": [
                ("математика", 95),
                ("физика", 89),
                ("химия", 92)
            ]
        }
        excellent_count = 2
        return data, excellent_count

    def test_init_calc_excellent_students(self, input_data: tuple[DataType, int]) -> None:
        calc = CalcExcellentStudents(input_data[0])
        assert input_data[0] == calc.data
        assert calc.excellent_count == 0

    def test_calc(self, input_data: tuple[DataType, int]) -> None:
        count = CalcExcellentStudents(input_data[0]).calc()
        assert count == input_data[1]