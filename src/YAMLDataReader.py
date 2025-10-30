# -*- coding: utf-8 -*-
import yaml
from Types import DataType
from DataReader import DataReader

class YAMLDataReader(DataReader):
    
    def read(self, path: str) -> DataType:
        with open(path, 'r', encoding='utf-8') as file:
            data = yaml.safe_load(file)
        
        students: DataType = {}
        
        for student_name, subjects in data.items():
            students[student_name] = []
            for subject, score in subjects.items():
                students[student_name].append((subject, int(score)))
        
        return students