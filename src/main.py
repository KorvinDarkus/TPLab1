# -*- coding: utf-8 -*-
import argparse
import sys
from CalcRating import CalcRating
from TextDataReader import TextDataReader
from YAMLDataReader import YAMLDataReader  # Добавляем импорт
from CalcExcellentStudents import CalcExcellentStudents  # Добавляем импорт


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str, required=True,
                      help="Path to datafile")
    parser.add_argument("-f", dest="format", type=str, default="txt",
                      help="File format (txt, yaml)")
    args = parser.parse_args(args)
    return args.path, args.format


def main():
    path, file_format = get_path_from_arguments(sys.argv[1:])
    
    if file_format == "yaml":
        reader = YAMLDataReader()
    else:
        reader = TextDataReader()
        
    students = reader.read(path)
    print("Students: ", students)
    
    rating = CalcRating(students).calc()
    print("Rating: ", rating)
    
    excellent_count = CalcExcellentStudents(students).calc()
    print(f"Excellent students count: {excellent_count}")


if __name__ == "__main__":
    main()