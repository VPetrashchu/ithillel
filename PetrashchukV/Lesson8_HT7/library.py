import csv
import re

# Task 2
def read_domains(filename="domains.txt"):
    with open(filename, 'r') as file:
        domains = [line.strip('.\n') for line in file]
    return domains

# Task 3
def match_authors_list(filename="authors.txt"):
    result = []
    pattern = re.compile(r'''
        (?:
            ([A-Z][a-z]+)'s
        )
        | 
        (?:
            by\s+
            (?:
                (?:
                    \w+\s+
                    ([A-Z][a-z]+)\s
                )
                |
                (?:
                    .+([A-Z][a-z]+),
                )
            )
        )
    ''', re.VERBOSE)

    with open(filename, 'r') as authors:
        for line in authors:
            author = re.search(pattern, line)
            if author:
                result.append(' '.join(filter(lambda name: name is not None, author.groups())))
    return list(set(result))

# Task 4
def read_author_dates(filename="authors.txt"):
    result = []
    date_pattern = re.compile(
        r'\b\d{1,2}(?:st|nd|rd|th)?\s+(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{4}\b')

    with open("authors.txt", 'r') as file:
        for line in file:
            match = re.search(date_pattern, line)
            if match:
                result.append({"date": match.group()})

    return result

# Task 5
def read_csv(filename="example.csv"):
    with open(filename, 'r') as file:
        csv_data = [line.strip().split(',') for line in file]
    return csv_data

def write_to_file(filename, data):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

