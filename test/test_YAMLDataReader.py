# -*- coding: utf-8 -*-
import pytest
import tempfile
import os
from src.Types import DataType
from src.YAMLDataReader import YAMLDataReader

class TestYAMLDataReader:
    
    @pytest.fixture()
    def file_and_data_content(self) -> tuple[str, DataType]:
        yaml_content = """
Иванов Иван Иванович:
  математика: 95
  программирование: 92
  литература: 90
Петров Петр Петрович:
  математика: 85
  химия: 80
Сидоров Сидор Сидорович:
  физика: 95
  математика: 96
  химия: 94
"""
        data = {
            "Иванов Иван Иванович": [
                ("математика", 95), ("программирование", 92), ("литература", 90)
            ],
            "Петров Петр Петрович": [
                ("математика", 85), ("химия", 80)
            ],
            "Сидоров Сидор Сидорович": [
                ("физика", 95), ("математика", 96), ("химия", 94)
            ]
        }
        return yaml_content, data

    @pytest.fixture()
    def filepath_and_data(self, file_and_data_content: tuple[str, DataType]) -> tuple[str, DataType]:

        with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False, encoding='utf-8') as f:
            f.write(file_and_data_content[0])
            temp_path = f.name
        
        yield temp_path, file_and_data_content[1]
        
        os.unlink(temp_path)

    def test_read(self, filepath_and_data: tuple[str, DataType]) -> None:
        file_content = YAMLDataReader().read(filepath_and_data[0])
        assert file_content == filepath_and_data[1]