import csv
import json


class CSVConverter:
    def __init__(self):
        self.__lines = []

    def read_file(self, filename:str):
        with open(filename, 'r') as csv_file:
            lines = csv.DictReader(csv_file)
            for line in lines:
                self.__lines.append(line)
            print(self.__lines)

    def write_file(self, filename:str):
        with open(filename, 'w', newline='') as writer:
            json.dump(self.__lines, writer, indent=4)
            self.cleanup()


    def cleanup(self):
        self.__lines=[]


converter = CSVConverter()
converter.read_file('example.csv')
converter.write_file('example.json')
converter.read_file('example.csv')
converter.write_file('example2.json')