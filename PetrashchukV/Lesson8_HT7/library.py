import csv
import re

#Task2
def read_domains(filename="domains.txt"):
    with open(filename, 'r') as file:
        domains = [line.strip() for line in file]
    return domains

#Task3
def read_surnames(filename="authors.txt"):
    with open(filename, 'r') as file:
        surnames = [line.split()[5] for line in file if re.match(r"\d+\w+\s\w+\s\d{4}", line)]
    return surnames

#Task4
def read_author_dates(filename="authors.txt"):
    author_dates = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip().split(' - ')[0]
            if line.isdigit():
                author_dates.append({"date": line})
    return author_dates

#Task5
def read_csv(filename="example.csv"):
    with open(filename, 'r') as file:
        csv_data = [line.strip().split(',') for line in file]
    return csv_data

def write_to_file(date, filename="modified_example.csv"):
    with open(filename, 'w') as file:
        for line in data:
            file.write(line + '\n')
