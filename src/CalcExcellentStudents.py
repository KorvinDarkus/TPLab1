# -*- coding: utf-8 -*-
from Types import DataType

class CalcExcellentStudents:
    
    def __init__(self, data: DataType) -> None:
        self.data: DataType = data
        self.excellent_count: int = 0

    def calc(self) -> int:
        self.excellent_count = 0
        
        for _, subjects in self.data.items():
            is_excellent = True
            for _, score in subjects:
                if score < 90:
                    is_excellent = False
                    break
            
            if is_excellent:
                self.excellent_count += 1
        
        return self.excellent_count